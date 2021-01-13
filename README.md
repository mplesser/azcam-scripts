# azcam-scripts

*azcam-scripts* is an *azcam* extension which adds general purpose scripts. These scripts are genreally intended for command line use. It may require a variety of azcam extensions to be installed, depeing on the script.

## Installation

`pip install azcam-scripts`

Or download from github: https://github.com/mplesser/azcam-scripts.git.

## Operation

The code below is for example only. The scripts are intended to be executed in an *azcam* IPython window.

Use `from azcam_scripts import xxx` to import module `xxx`. Scripts may then be executed by name as `xxx.xxx()`, for example, `get_temps.get_temps()`. A shortcut would by like `from azcam_scripts.get_temps import get_temps` and then execute with `get_temp()`.

In some cases it may be useful to bring all the script functions directly to the command line namespace. In this case, use
`from azcam_scripts.all_scripts import *`.


## Code

### Temperature Controller

`get_temps()`

### Controller

### Exposure

### Images
`check_bits("test.fits")`
