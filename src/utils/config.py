"""
Configuration management utilities.

Handles environment variables and configuration loading.
"""

import os
from pathlib import Path
from typing import Optional


class ConfigError(Exception):
    """Raised when configuration is invalid."""
    pass


class Config:
    """Configuration manager for application settings."""
    
    def __init__(self, env_file: Optional[Path] = None) -> None:
        """
        Initialize configuration.
        
        Args:
            env_file: Optional path to .env file
        """
        self.env_file = env_file
        if env_file and env_file.exists():
            self._load_env_file(env_file)
    
    def _load_env_file(self, path: Path) -> None:
        """
        Load environment variables from file.
        
        Args:
            path: Path to .env file
        """
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()
    
    def get(self, key: str, default: Optional[str] = None, required: bool = False) -> Optional[str]:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if not found
            required: Whether value is required
            
        Returns:
            Configuration value or default
            
        Raises:
            ConfigError: If required value is missing
        """
        value = os.environ.get(key, default)
        
        if required and value is None:
            raise ConfigError(f"Required configuration missing: {key}")
        
        return value
    
    def get_int(self, key: str, default: Optional[int] = None, required: bool = False) -> Optional[int]:
        """
        Get integer configuration value.
        
        Args:
            key: Configuration key
            default: Default value if not found
            required: Whether value is required
            
        Returns:
            Integer value or default
            
        Raises:
            ConfigError: If required value is missing or invalid
        """
        value_str = self.get(key, required=required)
        
        if value_str is None:
            return default
        
        try:
            return int(value_str)
        except ValueError as e:
            raise ConfigError(f"Invalid integer value for {key}: {value_str}") from e
    
    def get_bool(self, key: str, default: bool = False) -> bool:
        """
        Get boolean configuration value.
        
        Args:
            key: Configuration key
            default: Default value if not found
            
        Returns:
            Boolean value
        """
        value = self.get(key)
        
        if value is None:
            return default
        
        return value.lower() in ("true", "1", "yes", "on")
    
    def get_path(self, key: str, default: Optional[Path] = None, required: bool = False) -> Optional[Path]:
        """
        Get path configuration value.
        
        Args:
            key: Configuration key
            default: Default value if not found
            required: Whether value is required
            
        Returns:
            Path object or default
            
        Raises:
            ConfigError: If required value is missing
        """
        value = self.get(key, required=required)
        
        if value is None:
            return default
        
        return Path(value).expanduser().resolve()


# Global configuration instance
_config: Optional[Config] = None


def get_config(env_file: Optional[Path] = None) -> Config:
    """
    Get global configuration instance.
    
    Args:
        env_file: Optional path to .env file
        
    Returns:
        Configuration instance
    """
    global _config
    
    if _config is None:
        _config = Config(env_file)
    
    return _config
