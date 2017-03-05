from os import listdir
import os
import logging
from os.path import isfile, join

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def dynamic_analysis(filename, location):
    print location
    try:
        os.system(
        "docker run -it --rm -v %s:/samples/:ro -v %s/out:/samples/out honeynet/droidbox /samples/%s 100" %
        (location, location, filename))
        return True
    except (KeyboardInterrupt, SystemExit):
        logger.exception("Droidbox Timed Out")
