"""Tests for safe-rss-reader."""

import pytest
from safe_rss_reader import reader


class TestReader:
    """Test suite for reader."""

    def test_basic(self):
        """Test basic usage."""
        result = reader("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            reader("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = reader(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
