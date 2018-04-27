# Constants and functions for Marsaglia bits ingestion

# constants
FILE_BASE = '/media/alxfed/toca/bits.'
FILE_NUMBER_MIN = 1
FILE_NUMBER_MAX = 60

# pseudo-constants
FILE_EXTENSION = [str(i).zfill(2) for i in range(FILE_NUMBER_MIN, FILE_NUMBER_MAX + 1)]

# pseudo-function
def file_name(n=1):
    """
    if n is in the range of existing files - return the file name, else - except
    """
    if n in range(FILE_NUMBER_MIN, FILE_NUMBER_MAX+1):
        return FILE_BASE + FILE_EXTENSION[n-1]
    else:
        raise ValueError('There is no such file in Marsaglia')

print(file_name(1))