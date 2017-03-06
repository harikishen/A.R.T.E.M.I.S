from os import listdir
import os
import json
import logging
from os.path import isfile, join

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def jsonparse(location):
    def_actions = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    json_file = location + "out/analysis.json"
    status = os.path.isfile(json_file)
    if status:
        json_data = open(json_file)
        data = json.load(json_data)
        json_data.close()
        perm = []
        i = 0
        for item in data:
            perm.append(1 if len(data[item]) > 0 else 0)
        perm.pop(1)
        os.system("rm -r %s" % (location + "out"))
        return perm
    else:
        return def_actions

def dynamic_analysis(filename, location):
    print location
    try:
        os.system(
        "docker run -it --rm -v %s:/samples/:ro -v %s/out:/samples/out honeynet/droidbox /samples/%s 100" %
        (location, location, filename))
        return True
    except (KeyboardInterrupt, SystemExit):
        logger.exception("Droidbox Timed Out")
