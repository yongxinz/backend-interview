"""Shared pytest fixtures and configuration for all tests."""

import os
import sys
import tempfile
from pathlib import Path
from typing import Generator

import pytest


# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Provide a temporary directory for tests that need file operations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Provide a temporary file for tests."""
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("test content")
    yield temp_file


@pytest.fixture
def mock_env_vars():
    """Context manager for temporarily setting environment variables."""
    original_env = os.environ.copy()
    
    def _set_env(**kwargs):
        os.environ.update(kwargs)
        return os.environ
    
    yield _set_env
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "integers": [1, 2, 3, 4, 5],
        "strings": ["apple", "banana", "cherry"],
        "mixed": [1, "two", 3.0, True, None],
        "nested": {
            "list": [1, 2, 3],
            "dict": {"a": 1, "b": 2},
            "tuple": (1, 2, 3)
        }
    }


@pytest.fixture
def sample_tree_node():
    """Provide a sample binary tree node structure."""
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    return root


@pytest.fixture
def sample_linked_list_node():
    """Provide a sample linked list node structure."""
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
    
    return head


@pytest.fixture(autouse=True)
def reset_sys_modules():
    """Reset sys.modules to prevent module caching issues between tests."""
    modules_before = set(sys.modules.keys())
    yield
    modules_after = set(sys.modules.keys())
    for module in modules_after - modules_before:
        if module.startswith(("src", "编程题", "数据结构与算法")):
            del sys.modules[module]


@pytest.fixture
def capture_stdout(monkeypatch):
    """Capture stdout for testing print statements."""
    import io
    
    captured_output = io.StringIO()
    
    def _capture():
        monkeypatch.setattr("sys.stdout", captured_output)
        return captured_output
    
    return _capture


@pytest.fixture
def mock_input(monkeypatch):
    """Mock input() function for testing interactive code."""
    def _mock_input(inputs):
        input_iterator = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))
    
    return _mock_input


# Pytest hooks
def pytest_configure(config):
    """Configure pytest with custom settings."""
    # Add custom markers
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)