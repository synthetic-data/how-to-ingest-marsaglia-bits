# Filling a numpy ndarray with Marsaglia bits

import numpy as np
import supplement as supp


A = np.fromfile(supp.file_name(42), dtype=np.uint8, count=-1, sep="")

print(A)
print(len(A))

