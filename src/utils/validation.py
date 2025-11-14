"""
Input validation utilities.

Provides validation for string patterns, file paths, and other inputs.
"""

import re
from pathlib import Path
from typing import Optional


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


def validate_string_pattern(
    value: str,
    pattern: str,
    name: str = "value",
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
) -> str:
    """
    Validate string matches a regex pattern.
    
    Args:
        value: String to validate
        pattern: Regex pattern to match
        name: Name of the value for error messages
        min_length: Minimum string length
        max_length: Maximum string length
        
    Returns:
        The validated string
        
    Raises:
        ValidationError: If validation fails
    """
    if not isinstance(value, str):
        raise ValidationError(f"{name} must be a string, got {type(value).__name__}")
    
    if min_length is not None and len(value) < min_length:
        raise ValidationError(f"{name} must be at least {min_length} characters")
    
    if max_length is not None and len(value) > max_length:
        raise ValidationError(f"{name} must be at most {max_length} characters")
    
    if not re.match(pattern, value):
        raise ValidationError(f"{name} must match pattern: {pattern}")
    
    return value


def validate_file_path(
    path: str | Path,
    must_exist: bool = True,
    must_be_file: bool = True,
    must_be_dir: bool = False,
) -> Path:
    """
    Validate file path.
    
    Args:
        path: Path to validate
        must_exist: Whether path must exist
        must_be_file: Whether path must be a file
        must_be_dir: Whether path must be a directory
        
    Returns:
        Validated Path object
        
    Raises:
        ValidationError: If validation fails
    """
    path_obj = Path(path) if isinstance(path, str) else path
    
    if must_exist and not path_obj.exists():
        raise ValidationError(f"File not found: {path_obj}")
    
    if must_be_file and path_obj.exists() and not path_obj.is_file():
        raise ValidationError(f"Path is not a file: {path_obj}")
    
    if must_be_dir and path_obj.exists() and not path_obj.is_dir():
        raise ValidationError(f"Path is not a directory: {path_obj}")
    
    return path_obj


def validate_memory_key(key: str) -> str:
    """
    Validate hierarchical memory key format.
    
    Expected format: namespace:branch:feature:context_type
    Example: prompt_dna:main:001-repo-setup:patterns
    
    Args:
        key: Memory key to validate
        
    Returns:
        Validated key
        
    Raises:
        ValidationError: If key format is invalid
    """
    parts = key.split(":")
    if len(parts) != 4:
        raise ValidationError(
            f"Memory key must have format namespace:branch:feature:context_type, got: {key}"
        )
    
    namespace, branch, feature, context_type = parts
    
    # Validate each component
    if not re.match(r"^[a-zA-Z0-9_-]+$", namespace):
        raise ValidationError(f"Namespace must contain only alphanumeric, underscore, and hyphen characters: {namespace}")
    
    if not re.match(r"^[a-zA-Z0-9_-]+$", branch):
        raise ValidationError(f"Branch must contain only alphanumeric, underscore, and hyphen characters: {branch}")
    
    if not re.match(r"^[a-zA-Z0-9_-]+$", feature):
        raise ValidationError(f"Feature must contain only alphanumeric, underscore, and hyphen characters: {feature}")
    
    # Validate context type is one of the allowed values
    allowed_types = {"patterns", "context", "decisions", "constraints"}
    if context_type not in allowed_types:
        raise ValidationError(
            f"Context type must be one of {allowed_types}, got: {context_type}"
        )
    
    return key


def validate_language_support(language: str) -> str:
    """
    Validate programming language is supported.
    
    Per FR-019, only Python and Node.js are supported.
    
    Args:
        language: Programming language to validate
        
    Returns:
        Normalized language name
        
    Raises:
        ValidationError: If language not supported
    """
    supported = {"python", "javascript", "typescript", "nodejs", "node", "js", "ts", "py"}
    normalized = language.lower().strip()
    
    if normalized not in supported:
        raise ValidationError(
            f"Unsupported language: {language}. "
            f"Supported languages: Python, Node.js (JavaScript/TypeScript)"
        )
    
    # Normalize to standard names
    if normalized in {"py", "python"}:
        return "python"
    else:  # js, javascript, ts, typescript, nodejs, node
        return "nodejs"
