from vector import *
from nn import *
from rbm import *
import numpy as np
from config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

trX = np.loadtxt(VECTOR_STORE, np.float32)
trY = np.loadtxt(LABEL_STORE, np.float32)
RBM_hidden_sizes = [233, 200, 150, 100, 50]
inpX = trX
rbm_list = []
input_size = inpX.shape[1]

for i, size in enumerate(RBM_hidden_sizes):
    logger.info('RBM: ' + str(i) + ' ' + str(input_size) + '->' + str(size))
    rbm_list.append(RBM(input_size, size))
    input_size = size

for rbm in rbm_list:
    logger.info('New RBM:')
    # Train a new one
    rbm.train(inpX)
    # Return the output layer
    inpX = rbm.rbm_outpt(inpX)

nNet = NN(RBM_hidden_sizes, trX, trY)
nNet.load_from_rbms(RBM_hidden_sizes, rbm_list)
nNet.train()
