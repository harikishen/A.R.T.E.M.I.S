from vector import *
from nn import *
from rbm import *
from config import *

import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def createVector(filenames, location):
    global folderindex, vector, label
    for filename in filenames:
        logger.info(filename)
        temp_vector, temp_label = vectorize(filename, folderindex, location)
        if temp_vector:
            vector.append(temp_vector)
            label.append(temp_label)
        folderindex = folderindex + 1

folderindex = 0
vector = []
label = []

filenames = glob.glob(BENIGN_PATH + "*")
createVector(filenames, BENIGN_PATH)
filenames = glob.glob(MALWARE_PATH + "*")
createVector(filenames, MALWARE_PATH)

if vector and label:
    trX1 = np.array(vector, np.float32)
    trY1 = np.array(label, np.float32)
    trX2 = np.loadtxt(VECTOR_STORE, np.float32)
    trY2 = np.loadtxt(LABEL_STORE, np.float32)
    trX2 = np.concatenate((trX2, trX1), axis=0)
    trY2 = np.concatenate((trY2, trY1), axis=0)
    np.savetxt(VECTOR_STORE, trX2, fmt='%d')
    np.savetxt(LABEL_STORE, trY2, fmt='%d')
else:
    logger.warning('Empty Vector')
