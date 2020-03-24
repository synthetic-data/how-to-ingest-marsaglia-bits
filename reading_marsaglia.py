"""
Reading Marsaglia bits into statistical tests in Python
"""
import numpy as np


def bits_from_marsaglia_cd(np_array_shape = [], path_to_cd = ".", files_to_ing = [],
                           start_file=40):
    """
    This is a function that reads a Marsaglia file and creates a np.array of
    unsigned Marsaglia bytes comprised of Marsaglia bits.

    :param np_array_shape: list giving a shape of a desired np.array
    :param path_to_cd: path to the directory wher Marsaglia files are
    :param files_to_ing: the list of all Marsaglia files
    :param start_file: number of the start file in Marsaglia set
    :return: np array of given shape filled with Marsaglia bytes.
    """
    file_to_read = path_to_cd + "/" + files_to_ing[start_file]
    A = np.fromfile(file_to_read, dtype = np.int8,
                    count = np.prod(np_array_shape),
                    sep = "").reshape(np_array_shape)
    return A


if __name__ =='__main__':
    CD_PATH = '/media/alxfed/data/Marsaglia/cdrom'
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
    ASHAPE = [100, 100, 100]

    A = bits_from_marsaglia_cd(np_array_shape = ASHAPE,
                               path_to_cd = CD_PATH,
                               files_to_ing = FILES_TO_INGEST,
                               start_file = 44)
    B = A[88:95, 88:95, 88:95]
    print(B, "\n")
    print(A.shape)


