"""Package for unloading packages from memory."""

import sys

DEFAULT_RELOAD_PACKAGES: list[str] = []


def unload(packages=None, verbose=False):
    """Unload packages from memory.

    Args:
        packages (list[str], optional): List of packages to unload. Defaults to None.
        verbose (bool, optional): Print verbose output. Defaults to False.
    """
    if packages is None:
        packages = DEFAULT_RELOAD_PACKAGES

    reload_list = []
    for module in sys.modules.keys():
        for package in packages:
            if module.startswith(package):
                reload_list.append(module)

    for module in reload_list:
        try:
            if sys.modules[module] is not None:
                del sys.modules[module]
                if verbose:
                    print(f"Unloaded: {module}")
        except Exception as e:
            if verbose:
                print(f"Error unloading {module}: {e}")


if __name__ == "__main__":
    unload()
