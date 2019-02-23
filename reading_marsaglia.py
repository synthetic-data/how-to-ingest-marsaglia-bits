"""
Reading Marsaglia bits into statistical tests in Python
"""


import numpy as np
import os

def bits_from_marsaglia_cd(np_array='None',
                           path_to_cd=".",
                           files_to_ingest=['bits.01'],
                           word_length=8, n_words=10):
    """
    Reads bits from the files on Marsaglia CD ROM, combines them
    into words of predefined length and loads thm them into a numpy
    array.
    :param np_array:
    :param path_to_cd:
    :param files_to_ingest:
    :param word_length:
    :param n_words:
    :return: np_array filled with Marsaglia random bits
    """

file_to_read = open('/media/alxfed/toca/bits.42', mode="rb")
a = file_to_read.read(100)
out = file_to_read.close()

printable_bytes = [int(x) for x in a]
# or printable_bytes = [int(x) for x in a if x < 10]

print(printable_bytes[0:9])

if __name__ =='__main__':
    CD_PATH = '/media/alxfed/toca/toshiba_new_archive/Marsaglia/cdrom'
    FILES_TO_INGEST = ['bits.01', 'bits.02', 'bits.03', 'bits.04',
                       'bits.05', 'bits.06', 'bits.07', 'bits.08',
                       'bits.09', 'bits.10', 'bits.11', 'bits.12',
                       'bits.13', 'bits.14', 'bits.15', 'bits.16',
                       'bits.17', 'bits.18', 'bits.19', 'bits.20',
                       'bits.21', 'bits.22', 'bits.23', 'bits.24',
                       'bits.25', 'bits.26', 'bits.27', 'bits.28',
                       'bits.29', 'bits.30', 'bits.31', 'bits.32',
                       'bits.33', 'bits.34', 'bits.35', 'bits.36',
                       'bits.37', 'bits.38', 'bits.39', 'bits.40',
                       'bits.41', 'bits.42', 'bits.43', 'bits.44',
                       'bits.45', 'bits.46', 'bits.47', 'bits.48',
                       'bits.49', 'bits.50', 'bits.51', 'bits.52',
                       'bits.53', 'bits.54', 'bits.55', 'bits.56',
                       'bits.57', 'bits.58', 'bits.59', 'bits.60']
    A = np.zeros((100,100,100), dtype = numpy.int8)
