# Filling a numpy ndarray with Marsaglia bits

import numpy as np
import supplement as supp

# Define a shape, read, then - reshape
# shape = (4, 4, 4, 4)
shape = (4, 100)

A = np.fromfile(
        supp.file_name(42),
        dtype = np.uint8,
        count = 400,
        sep = ""
    ).reshape(shape)

# we can turn it back and forth between the 1-d and shape with:
# 1. np.ravel(x, order = 'C,F,A,K') or
# 2  making a copy with np.flatten(order = 'C,F,A,K')

# reading slices
#def read_slice(filename, shape):
    # shape = (ndim,ndim,ndim)
#    fd = open(filename, 'rb')
#    fd = seek...
#    data = np.fromfile(file=fd, dtype=np.uint8).reshape(shape)
#    fd.close()
#    return data
