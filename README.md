# Python package reloader

Taken from Aleksandar Kocić's [website](https://www.aleksandarkocic.com/2020/12/19/live-reload-your-python-code-in-maya/).
It unloads any specified python packages currently imported in Maya, Unreal Engine, or another DCC, and allows for a clean reimport.

As he notes, this should only be used in development, and should not be used in production code or tools.

## Installation

### Installing with pip

```bash
pip install unload_packages
```

### Manual installation

Download the latest version from the [releases page](https://github.com/gabrieljreed/MayaPackageReloader/releases) and extract the `unload_packages` folder to your Maya scripts directory. (e.g. `C:\Users\username\Documents\maya\scripts`)

## Usage

In the Maya script editor, add this code to the top of your script:

```python
from unload_packages import unload
unload(["my_package", "my_other_package"])

import my_package
import my_other_package
...
```
