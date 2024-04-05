# Maya Python package reloader
Taken from Aleksandar Kocić's website, which can be found [here](https://www.aleksandarkocic.com/2020/12/19/live-reload-your-python-code-in-maya/).
It unloads any specified python packages currently imported in Maya and allows for a clean reimport.

## Installation
Clone this repository into the Maya scripts folder (usually found in Documents/maya/20XX/scripts)
```
git clone git@github.com:gabrieljreed/MayaPackageReloader.git
```

## Usage
In the Maya script editor, add this code to the top of your script:
```python
from unload_packages import unload_packages
unload_packages(silent=False, packages="myPackage")

from myPackage import myPackage
...
```
