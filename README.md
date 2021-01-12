# azcam-scripts

*azcam-scripts* is an *azcam* extension which adds general purpose scripts. These scripts are genreally intended for command line use. It may require a variety of azcam extensions to be installed, depeing on the script.

## Installation

`pip install azcam-scripts`

Or download from github: https://github.com/mplesser/azcam-scripts.git.

## Operation

The code below is for example only.  Usually the scripts are execuited in an *azcam* IPython window which defines the `Run` command.

Use `from azcam_scripts import xxx` to import function `xxx` into the current namespace.  Even more useful would be to issue `from azcam_scripts import *` to bring all the commands directly to the command line namespace.

Scripts may then be executed by name as `get_temps()`.

## Code

### Temperature Controller

`get_temps()`

### Controller

### Exposure

### Images
`check_bits("test.fits")`
