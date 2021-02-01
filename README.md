# AzCam Scripts Package - azcam-scripts

*azcam-scripts* is an *azcam* extension which adds general purpose scripts. These scripts are intended for command line use. A variety of azcam extensions may need to be installed for proper operation, depending on the script.

## Installation

`pip install azcam-scripts`

Or download from github: https://github.com/mplesser/azcam-scripts.git.

## Operation

The code below is for example only. The scripts are intended to be executed in an *azcam* IPython window.

Use `from azcam_scripts import xxx` to import module `xxx`. Scripts may then be executed by name as `xxx.xxx(10)`, for example, `get_temps.get_temps(10)`. A shortcut could be simialr to `from azcam_scripts.get_temps import get_temps` and then execute with `get_temps(10)`.

In some cases the environment setup configuration may bring all the script functions directly to the command line namespace. In this case, use just `get_temps(10)`.

Some environments may be configured to allow running scripts using IPython's magic syntax, such as `Run get_temps 10` where `Run` is a modification of the IPython `run` command which uses the current search path to find modules and does not require the *.py* file extension.  


# Scripts

### Temperature Controller

`get_temps()`

### Controller

### Exposure

### Images
`check_bits("test.fits")`
