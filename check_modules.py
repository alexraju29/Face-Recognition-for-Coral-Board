import importlib
import pkg_resources

def check_module_versions(modules):
    """
    Check the versions of the given list of Python modules.

    Args:
        modules (list): A list of module names to check.
    """
    for module in modules:
        try:
            # Attempt to import the module
            imported_module = importlib.import_module(module)
            # If import is successful, get the version
            version = getattr(imported_module, '__version__', 'Version not found')
            print(f"{module}: {version}")
        except ImportError:
            # Handle the case where the module is not installed
            print(f"{module}: Not installed")
        except Exception as e:
            # Handle any unexpected errors
            print(f"{module}: Error ({e})")

if __name__ == "__main__":
    # List of common Python modules to check
    modules_to_check = [
        "numpy", "opencv-python", "tensorflow", "flask", "scikit-learn", "matplotlib",
        "pandas", "scipy", "torch", "cv2", "setuptools", "pip", "pytest"
    ]

    print("Checking Python module versions...\n")
    check_module_versions(modules_to_check)