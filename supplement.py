# Constants and functions for Marsaglia bits ingestion

# constants
FILE_BASE = '/media/alxfed/toca/bits.'
FILE_NUMBER_MIN = 1
FILE_NUMBER_MAX = 60

# pseudo-constants
FILE_EXTENSION = [str(i).zfill(2) for i in range(FILE_NUMBER_MIN, FILE_NUMBER_MAX + 1)]
# starts with 0 element and ends with 59, that's why the dance in the function

# pseudo-function
def file_name(n=1):
    if n in range(FILE_NUMBER_MIN, FILE_NUMBER_MAX+1):  # +1 because...
        return FILE_BASE + FILE_EXTENSION[n-1]          # -1 because...
    else:
        raise ValueError('There is no such file in Marsaglia set of bits')


print(file_name(1))
