"""Tests for the package version."""

import importlib.metadata

import pydantic_config


def test_version_is_the_installed_distributions():
    assert pydantic_config.__version__ == importlib.metadata.version("prime-pydantic-config")
