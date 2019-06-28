# QuickLog

A sweet little logging module for python!

The FileHandler logs everything, StreamHandler brings errors level ERROR or higher to your console!


## Installation:

1. Download the quicklog.py module
2. Place it in your python environment or your project folder


## Basic usage:

Code example:

from quicklog import QuickLog

logger = QuickLog('mylogfile.log', 'myhost', 'myapp')
logger.log(0, 'Debug MSG')
logger.log(4, 'Critical MSG')


## Advanced Usage:
Any logger.xy() function refers to the code example above!

### Need Help?
logger.help() displays a basic usage example and all the log-levels!


### Exporting your logfile:
If you need to do a backup or export your logfile, you can use logger.export('/path/to/file.log').


### Display LogLevels:
If you're not sure which level you should log to, you can use logger.getlevels() to display all available levels.


### Modify Formatting:
On line 28 you find the formatter. Here you can modify the maximum whitespace of your different columns by modifying the following part: '%(asctime)s - %(name)-16s - %(levelname)-8s - %(message)s'
