import json
import glob
import tensorflow as tf
import os
import glob
import logging
from config import *
from extract import *
from config import *
from dexparse import *
from sandbox import *


def vectorize(filename, folderindex, location):
    os.chdir(INTEGRATED_PATH)
    file = open('WATCH_LIST')    # File containing the watchlist
    index = 0
    permission_index = {}
    permission_list = file.read().split('\n')

    for x in permission_list:   # Buliding an indexed list or associative array
        permission_index[x] = index
        index = index + 1

    file.close()
    file = open('SENSITIVE_APIS')    # File containing the sensitive APIs
    index = 0
    apicalls_index = {}
    apicalls_list = file.read().split('\n')

    for x in apicalls_list:     # Buliding an indexed list or associative array
        apicalls_index[x] = index
        index = index + 1

    file.close()

    vector = []
    label = []
    vector_apicalls = []
    dir = filename.split('/')[-1]
    permissions = extract(dir, folderindex, location)
    apicalls = dexparse(DEST_PATH + str(folderindex))
    # removing extrafolders
    os.system("rm -r %s" % (DEST_PATH + str(folderindex)))
    status = dynamic_analysis(dir, location)
    actions = jsonparse(location)
    listing = []
    current_app = []
    current_app_permission = permissions
    for x in range(0, len(permission_list), 1):
        listing.append(0)
    for x in current_app_permission:
        if x in permission_index.keys():
            listing[permission_index[x]] = 1
    vector.append(listing)
    listing = []
    current_app_apicalls = apicalls
    if current_app_apicalls:
        current_app_apicalls.pop()
    for x in range(0, len(apicalls_list), 1):
        listing.append(0)
    for x in current_app_apicalls:
        if x in apicalls_index.keys():
            listing[apicalls_index[x]] = 1
    vector_apicalls.append(listing)
    for x in range(0, len(vector), 1):
        if actions and permissions and apicalls:
            vector[x] = vector[x] + vector_apicalls[x] + actions
            if all(feature == 0 for feature in vector[x]):
                return False, False
            else:
                if str(location).split('/')[-2] == 'Benign':
                    label.append([0, 1])
                else:
                    label.append([1, 0])
                return vector[0], label[0]
        else:
            return False, False
