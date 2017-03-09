from predict import *
from vector import *
from config import *
import numpy as np
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

filename = sys.argv[1]
_vector = []
_label = []
logger.info(filename)
temp_vector, temp_label = vectorize(filename, 0, TEST_DATA_LOCATION)
if temp_vector:
    _vector.append(temp_vector)
    _label.append(temp_label)
logger.info(_vector)
logger.info(_label)
if _vector:
    logger.info(np.array(_vector, np.float32))
    print predict(np.array(_vector, np.float32))
else:
    logger.info("Empty Vector")
