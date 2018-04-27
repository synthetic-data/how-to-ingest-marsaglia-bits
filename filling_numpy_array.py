# Filling a numpy ndarray with Marsaglia bits

import numpy as np
import supplement as supp

#file_to_read = open(supp.file_name(1), mode="rb")

A = np.fromfile(supp.file_name(42), dtype=np.uint8, count=-1, sep="")
#a = file_to_read.read()
#out = file_to_read.close()

print(A)
print(len(A))

pass
