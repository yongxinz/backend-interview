"""Example unit test to demonstrate the testing infrastructure."""

import pytest


class TestExampleUnit:
    """Example unit test class to show how to structure tests."""
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        assert 2 + 2 == 4
        assert 10 - 5 == 5
        assert 3 * 4 == 12
        assert 15 / 3 == 5
    
    def test_string_operations(self):
        """Test string operations."""
        text = "Hello, World!"
        assert text.lower() == "hello, world!"
        assert text.upper() == "HELLO, WORLD!"
        assert text.replace("World", "Python") == "Hello, Python!"
    
    def test_list_operations(self):
        """Test list operations."""
        numbers = [1, 2, 3, 4, 5]
        assert len(numbers) == 5
        assert sum(numbers) == 15
        assert max(numbers) == 5
        assert min(numbers) == 1
    
    def test_using_fixtures(self, sample_data):
        """Test using fixtures from conftest.py."""
        assert "integers" in sample_data
        assert sample_data["integers"] == [1, 2, 3, 4, 5]
        assert len(sample_data["strings"]) == 3
    
    def test_with_parametrize(self):
        """Test using pytest parametrize."""
        @pytest.mark.parametrize("input,expected", [
            (1, 2),
            (2, 4),
            (3, 6),
            (4, 8),
        ])
        def double(x):
            return x * 2
        
        assert double(5) == 10
    
    def test_exception_handling(self):
        """Test exception handling."""
        with pytest.raises(ZeroDivisionError):
            1 / 0
        
        with pytest.raises(ValueError, match="invalid literal"):
            int("not a number")
    
    def test_using_mock(self, mocker):
        """Test using mock from pytest-mock."""
        # Mock a function
        mock_func = mocker.Mock(return_value="mocked result")
        
        result = mock_func("any", "arguments")
        assert result == "mocked result"
        mock_func.assert_called_once_with("any", "arguments")