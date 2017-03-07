import numpy as np
import math
import tensorflow as tf
import logging
import os
from config import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def predict(X):
    wlist = np.load(MODEL_STORE + 'weights.npy')
    blist = np.load(MODEL_STORE + 'bias.npy')
    sizes = np.load(MODEL_STORE + 'size.npy')
    _a = [None] * (len(sizes) + 2)
    _w = [None] * len(wlist)
    _b = [None] * len(blist)
    _a[0] = tf.placeholder("float", [None, X.shape[1]])
    for i in range(len(wlist)):
        _w[i] = tf.constant(np.array(wlist[i], np.float32))
        _b[i] = tf.constant(np.array(blist[i], np.float32))
    for i in range(1, len(sizes) + 2):
        _a[i] = tf.nn.sigmoid(tf.matmul(_a[i - 1], _w[i - 1]) + _b[i - 1])
    predict_op = tf.argmax(_a[-1], 1)
    with tf.Session() as sess:
        os.chdir(INTEGRATED_PATH)
        sess.run(tf.initialize_all_variables())
        return sess.run(predict_op, feed_dict={_a[0]: X})
