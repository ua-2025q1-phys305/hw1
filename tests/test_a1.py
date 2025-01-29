# This is a pytest script to test the package import for Assignment 1.
# It ensures that the module structure and dependencies (pyproject.toml, etc.)
# are set up correctly so that the required submodules can be imported.

def test_import():
    """Test whether the module structure is correctly configured for
    imports.

    This test checks if the package `phys305_hw1` is properly
    installed and if its submodules (a2, a3, a4) can be successfully
    imported.

    If `pyproject.toml` and other configuration files are correctly
    set up, the following import should work without errors.

    """
    try:
        from phys305_hw1 import a2, a3, a4  # Import required submodules
    except ImportError as e:
        assert False, f"Module import failed: {e}"
