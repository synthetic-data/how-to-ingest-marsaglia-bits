# Filling a numpy ndarray with Marsaglia bits

import numpy as np
import supplement as supp

# Define a shape, read, then - reshape
shape = (4, 4, 4, 4)
A = np.fromfile(
        supp.file_name(42),
        dtype = np.uint8,
        count = 256,
        sep = ""
    ).reshape(shape)

print(A[:, 0, 0, 0])
print(A[:, ...])

# reading slices
#def read_slice(filename, shape):
    # shape = (ndim,ndim,ndim)
#    fd = open(filename, 'rb')
#    data = np.fromfile(file=fd, dtype=np.uint8).reshape(shape)
#    fd.close()
#    return data
