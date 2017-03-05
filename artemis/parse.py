import os
import json


def jsonparse(location):
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
        return False
