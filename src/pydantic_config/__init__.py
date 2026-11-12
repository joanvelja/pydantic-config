from importlib.metadata import version as _version

__version__ = _version("prime-pydantic-config")

from pydantic_config.cli import cli, BaseConfig, ConfigFileError

__all__ = ["cli", "BaseConfig", "ConfigFileError"]
