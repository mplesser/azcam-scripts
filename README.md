# azcam-scripts

*azcam-scripts* is an *azcam* extension which adds general purpose scripts. It may require a variety of azcam extensions to be installed, depeing on the script.

## Installation

`pip install azcam-scripts`

Or download from github: https://github.com/mplesser/azcam-scripts.git.

## Example Code

The code below is for example only.  We assume the scipt is being run in an IPython azcam console window.

### Temperature Controller
    Run azcam_scripts.get_temps

### Controller
    controller = ControllerMag()
    controller.camserver.set_server(guider_address, guider_port)
    controller.timing_file = os.path.join(azcam.db.datafolder, "dspcode/gcam_ccd57.s")

### Exposure
    exposure = ExposureMag()
    filetype = "BIN"
    exposure.filetype = azcam.db.filetypes[filetype]
    exposure.image.filetype = azcam.db.filetypes[filetype]
    exposure.display_image = 1
    exposure.image.remote_imageserver_flag = 0
    exposure.set_name("/azcam/soguider/image.bin")
    exposure.test_image = 0
    exposure.root = "image"
    exposure.display_image = 0
    exposure.image.make_lockfile = 1
