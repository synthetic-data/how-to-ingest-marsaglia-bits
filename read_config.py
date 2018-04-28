# Using configparser (the version for Python 3.)
# https://pymotw.com/3/configparser/

from configparser import ConfigParser

# Constants
CONFIG_FILE_NAME = 'data_config.ini'

parser = ConfigParser()

if not parser.read(CONFIG_FILE_NAME):           # no file yet, create one
    file_to_write = open(CONFIG_FILE_NAME, mode="x")
    parser.add_section('data_ndarray')
    parser.set('data_ndarray', 'x', '3')
    parser.set('data_ndarray', 'y', '4')
    parser.set('data_ndarray', 'z', '5')
    parser.write(file_to_write)
    out = file_to_write.close()

else:                           # file read, start parsing
    parser.read(CONFIG_FILE_NAME)
