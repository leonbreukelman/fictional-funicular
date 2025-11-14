"""
Unit tests for utility modules.

Tests logging, validation, and config utilities.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import structlog

from src.utils.config import Config, ConfigError, get_config
from src.utils.logging import configure_logging, get_logger
from src.utils.validation import (
    ValidationError,
    validate_file_path,
    validate_language_support,
    validate_memory_key,
    validate_string_pattern,
)


class TestLogging:
    """Test logging utilities."""
    
    def test_configure_logging(self):
        """Test logging configuration."""
        configure_logging()
        assert structlog.is_configured()
    
    def test_get_logger(self):
        """Test logger creation."""
        logger = get_logger("test")
        assert logger is not None
    
    def test_logger_with_context(self):
        """Test logger with context."""
        logger = get_logger("test")
        bound_logger = logger.bind(user_id="123")
        assert bound_logger is not None
    
    def test_configure_logging_json_format(self):
        """Test logging configuration with JSON format."""
        os.environ["LOG_FORMAT"] = "json"
        try:
            configure_logging()
            logger = get_logger("test_json")
            # Verify logger works with JSON format
            assert logger is not None
        finally:
            if "LOG_FORMAT" in os.environ:
                del os.environ["LOG_FORMAT"]
    
    def test_configure_logging_debug_level(self):
        """Test logging configuration with DEBUG level."""
        os.environ["LOG_LEVEL"] = "DEBUG"
        try:
            configure_logging()
            logger = get_logger("test_debug")
            # Verify logger works with DEBUG level
            assert logger is not None
        finally:
            if "LOG_LEVEL" in os.environ:
                del os.environ["LOG_LEVEL"]
    
    def test_add_correlation_id_new(self):
        """Test adding new correlation ID."""
        from src.utils.logging import add_correlation_id
        import logging as std_logging
        
        logger = std_logging.getLogger("test")
        event_dict = {"event": "test_event"}
        result = add_correlation_id(logger, "info", event_dict)
        
        assert "correlation_id" in result
        assert isinstance(result["correlation_id"], str)
    
    def test_add_correlation_id_existing(self):
        """Test preserving existing correlation ID."""
        from src.utils.logging import add_correlation_id
        import logging as std_logging
        
        logger = std_logging.getLogger("test")
        existing_id = "existing-correlation-id"
        event_dict = {"event": "test_event", "correlation_id": existing_id}
        result = add_correlation_id(logger, "info", event_dict)
        
        assert result["correlation_id"] == existing_id


class TestValidation:
    """Test validation utilities."""
    
    def test_validate_string_pattern_valid(self):
        """Test valid string pattern."""
        validate_string_pattern("test123", r"^[a-z0-9]+$", "test")
    
    def test_validate_string_pattern_invalid(self):
        """Test invalid string pattern."""
        with pytest.raises(ValidationError, match="test must match pattern"):
            validate_string_pattern("Test!", r"^[a-z0-9]+$", "test")
    
    def test_validate_string_pattern_too_short(self):
        """Test string too short."""
        with pytest.raises(ValidationError, match="test must be at least 3 characters"):
            validate_string_pattern("ab", r"^[a-z]+$", "test", min_length=3)
    
    def test_validate_string_pattern_too_long(self):
        """Test string too long."""
        with pytest.raises(ValidationError, match="test must be at most 5 characters"):
            validate_string_pattern("abcdefg", r"^[a-z]+$", "test", max_length=5)
    
    def test_validate_string_pattern_non_string(self):
        """Test non-string value."""
        with pytest.raises(ValidationError, match="test must be a string"):
            validate_string_pattern(123, r"^[0-9]+$", "test")
    
    def test_validate_file_path_valid(self):
        """Test valid file path."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = Path(f.name)
        
        try:
            validate_file_path(path)
        finally:
            path.unlink()
    
    def test_validate_file_path_not_found(self):
        """Test non-existent file path."""
        with pytest.raises(ValidationError, match="File not found"):
            validate_file_path(Path("/nonexistent/file.txt"))
    
    def test_validate_file_path_not_file(self):
        """Test directory path."""
        with tempfile.TemporaryDirectory() as d:
            with pytest.raises(ValidationError, match="Path is not a file"):
                validate_file_path(Path(d))
    
    def test_validate_file_path_directory(self):
        """Test validating directory path."""
        with tempfile.TemporaryDirectory() as d:
            path = validate_file_path(Path(d), must_be_file=False, must_be_dir=True)
            assert path.is_dir()
    
    def test_validate_file_path_no_checks(self):
        """Test file path with no existence checks."""
        path = validate_file_path("/nonexistent/path", must_exist=False, must_be_file=False)
        assert isinstance(path, Path)
    
    def test_validate_file_path_dir_not_dir(self):
        """Test non-directory path when directory required."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            path = Path(f.name)
        
        try:
            with pytest.raises(ValidationError, match="Path is not a directory"):
                validate_file_path(path, must_be_file=False, must_be_dir=True)
        finally:
            path.unlink()
    
    def test_validate_memory_key_valid(self):
        """Test valid memory key."""
        validate_memory_key("myrepo:main:feature:patterns")
    
    def test_validate_memory_key_invalid_format(self):
        """Test invalid memory key format."""
        with pytest.raises(ValidationError, match="Memory key must have format"):
            validate_memory_key("invalid")
    
    def test_validate_memory_key_invalid_namespace(self):
        """Test invalid namespace characters."""
        with pytest.raises(ValidationError, match="Namespace must contain only"):
            validate_memory_key("My Repo!:main:feature:patterns")
    
    def test_validate_memory_key_invalid_branch(self):
        """Test invalid branch characters."""
        with pytest.raises(ValidationError, match="Branch must contain only"):
            validate_memory_key("myrepo:main branch:feature:patterns")
    
    def test_validate_memory_key_invalid_feature(self):
        """Test invalid feature characters."""
        with pytest.raises(ValidationError, match="Feature must contain only"):
            validate_memory_key("myrepo:main:my feature!:patterns")
    
    def test_validate_memory_key_invalid_context_type(self):
        """Test invalid context type."""
        with pytest.raises(ValidationError, match="Context type must be one of"):
            validate_memory_key("myrepo:main:feature:invalid_type")
    
    def test_validate_language_support_python(self):
        """Test Python language support."""
        validate_language_support("python")
    
    def test_validate_language_support_javascript(self):
        """Test JavaScript language support."""
        validate_language_support("javascript")
    
    def test_validate_language_support_unsupported(self):
        """Test unsupported language."""
        with pytest.raises(ValidationError, match="Unsupported language"):
            validate_language_support("cobol")
    
    def test_validate_language_support_typescript(self):
        """Test TypeScript language support."""
        result = validate_language_support("typescript")
        assert result == "nodejs"
    
    def test_validate_language_support_normalized(self):
        """Test language normalization."""
        assert validate_language_support("py") == "python"
        assert validate_language_support("Python") == "python"
        assert validate_language_support("JAVASCRIPT") == "nodejs"
        assert validate_language_support("ts") == "nodejs"


class TestConfig:
    """Test configuration utilities."""
    
    def test_config_get_existing(self):
        """Test getting existing environment variable."""
        os.environ["TEST_VAR"] = "value"
        
        try:
            config = Config()
            assert config.get("TEST_VAR") == "value"
        finally:
            del os.environ["TEST_VAR"]
    
    def test_config_get_default(self):
        """Test getting default value."""
        config = Config()
        assert config.get("NONEXISTENT", default="default") == "default"
    
    def test_config_get_required_missing(self):
        """Test required value missing."""
        config = Config()
        with pytest.raises(ConfigError, match="Required configuration missing"):
            config.get("NONEXISTENT", required=True)
    
    def test_config_get_int(self):
        """Test getting integer value."""
        os.environ["TEST_INT"] = "42"
        
        try:
            config = Config()
            assert config.get_int("TEST_INT") == 42
        finally:
            del os.environ["TEST_INT"]
    
    def test_config_get_int_invalid(self):
        """Test getting invalid integer."""
        os.environ["TEST_INT"] = "not_a_number"
        
        try:
            config = Config()
            with pytest.raises(ConfigError, match="Invalid integer value"):
                config.get_int("TEST_INT")
        finally:
            del os.environ["TEST_INT"]
    
    def test_config_get_bool_true(self):
        """Test getting boolean true values."""
        test_values = ["true", "True", "1", "yes", "on"]
        
        for value in test_values:
            os.environ["TEST_BOOL"] = value
            
            try:
                config = Config()
                assert config.get_bool("TEST_BOOL") is True
            finally:
                del os.environ["TEST_BOOL"]
    
    def test_config_get_bool_false(self):
        """Test getting boolean false values."""
        test_values = ["false", "False", "0", "no", "off"]
        
        for value in test_values:
            os.environ["TEST_BOOL"] = value
            
            try:
                config = Config()
                assert config.get_bool("TEST_BOOL") is False
            finally:
                del os.environ["TEST_BOOL"]
    
    def test_config_get_bool_default(self):
        """Test getting boolean default value."""
        config = Config()
        assert config.get_bool("NONEXISTENT_BOOL") is False
        assert config.get_bool("NONEXISTENT_BOOL", default=True) is True
    
    def test_config_get_path(self):
        """Test getting path value."""
        os.environ["TEST_PATH"] = "/tmp/test"
        
        try:
            config = Config()
            path = config.get_path("TEST_PATH")
            assert isinstance(path, Path)
            assert path == Path("/tmp/test").resolve()
        finally:
            del os.environ["TEST_PATH"]
    
    def test_config_load_env_file(self):
        """Test loading from .env file."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".env") as f:
            f.write("ENV_VAR1=value1\n")
            f.write("ENV_VAR2=value2\n")
            f.write("# Comment line\n")
            f.write("\n")
            env_file = Path(f.name)
        
        try:
            config = Config(env_file=env_file)
            assert config.get("ENV_VAR1") == "value1"
            assert config.get("ENV_VAR2") == "value2"
        finally:
            env_file.unlink()
            if "ENV_VAR1" in os.environ:
                del os.environ["ENV_VAR1"]
            if "ENV_VAR2" in os.environ:
                del os.environ["ENV_VAR2"]
    
    def test_get_config_singleton(self):
        """Test global config instance."""
        config1 = get_config()
        config2 = get_config()
        assert config1 is config2
    
    def test_config_get_int_default(self):
        """Test getting default integer value."""
        config = Config()
        assert config.get_int("NONEXISTENT_INT", default=99) == 99
    
    def test_config_get_path_default(self):
        """Test getting default path value."""
        config = Config()
        default_path = Path("/default/path")
        assert config.get_path("NONEXISTENT_PATH", default=default_path) == default_path.resolve()
    
    def test_config_get_required_int_missing(self):
        """Test required integer value missing."""
        config = Config()
        with pytest.raises(ConfigError, match="Required configuration missing"):
            config.get_int("NONEXISTENT_INT", required=True)
    
    def test_config_get_path_required_missing(self):
        """Test required path value missing."""
        config = Config()
        with pytest.raises(ConfigError, match="Required configuration missing"):
            config.get_path("NONEXISTENT_PATH", required=True)
