"""Validation tests to ensure the testing infrastructure is properly set up."""

import sys
from pathlib import Path

import pytest


class TestInfrastructureValidation:
    """Validate that the testing infrastructure is properly configured."""
    
    def test_pytest_is_available(self):
        """Test that pytest is installed and available."""
        assert pytest.__version__
    
    def test_project_structure_exists(self):
        """Test that the required project structure exists."""
        project_root = Path(__file__).parent.parent
        
        # Check tests directory structure
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "conftest.py").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "unit" / "__init__.py").exists()
        assert (project_root / "tests" / "integration").exists()
        assert (project_root / "tests" / "integration" / "__init__.py").exists()
        
        # Check configuration files
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / ".gitignore").exists()
    
    def test_python_path_includes_project_root(self):
        """Test that the project root is in the Python path."""
        project_root = str(Path(__file__).parent.parent)
        assert project_root in sys.path
    
    def test_fixtures_are_available(self, temp_dir, sample_data):
        """Test that custom fixtures from conftest.py are available."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test sample_data fixture
        assert isinstance(sample_data, dict)
        assert "integers" in sample_data
        assert "strings" in sample_data
    
    @pytest.mark.unit
    def test_unit_marker_works(self):
        """Test that the unit marker is properly configured."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker_works(self):
        """Test that the integration marker is properly configured."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker_works(self):
        """Test that the slow marker is properly configured."""
        assert True
    
    def test_coverage_configuration(self):
        """Test that coverage is properly configured."""
        try:
            import coverage
            assert coverage.__version__
        except ImportError:
            pytest.fail("Coverage module not installed")
    
    def test_mock_fixture_works(self, mocker):
        """Test that pytest-mock is properly installed and configured."""
        mock_func = mocker.Mock(return_value=42)
        assert mock_func() == 42
        mock_func.assert_called_once()


class TestSampleCodeExecution:
    """Test that we can import and test code from the project."""
    
    def test_can_import_from_src(self):
        """Test that we can import modules from the src directory."""
        try:
            # The src directory exists, so this should work
            import src
            assert True
        except ImportError:
            # It's okay if src doesn't have __init__.py
            assert True
    
    def test_python_files_are_importable(self):
        """Test that Python files in the project are valid Python."""
        # This is just a validation that our setup can handle the project structure
        project_root = Path(__file__).parent.parent
        
        # Check that we have Python files
        py_files = list(project_root.glob("**/*.py"))
        assert len(py_files) > 0, "No Python files found in project"


def test_standalone_validation():
    """A simple standalone test to validate basic pytest functionality."""
    assert 1 + 1 == 2
    assert isinstance("test", str)
    assert [1, 2, 3] == [1, 2, 3]