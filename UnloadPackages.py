import sys


DEFAULT_RELOAD_PACKAGES = []


def unloadPackages(silent=True, packages=None):
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
                if not silent:
                    print(f"Unloaded: {module}")
        except Exception as e:
            if silent:
                pass
            else:
                print(f"Error unloading {module}: {e}")


if __name__ == "__main__":
    unloadPackages()
