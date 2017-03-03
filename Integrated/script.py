from os import listdir
import os
from os.path import isfile, join


def dynamic_analysis(filename, location):
    print location
    os.system(
        "sudo docker run -it --rm -v %s:/samples/:ro -v %s/out:/samples/out honeynet/droidbox /samples/%s 100" %
        (location, location, filename))
    return True
