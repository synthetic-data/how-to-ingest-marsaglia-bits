# Using configparser (the version for Python 3.)
# https://pymotw.com/3/configparser/

from configparser import ConfigParser

# Constants
CONFIG_FILE_NAME = 'data_config.ini'

parser = ConfigParser()

if not parser.read(CONFIG_FILE_NAME):           # no file yet, create one
    file_to_write = open(CONFIG_FILE_NAME, mode="x")
    parser.add_section('data_array')
    parser.set('data_array', 'x', '3')
    parser.set('data_array', 'y', '4')
    parser.set('data_array', 'z', '5')
    parser.write(file_to_write)
    out = file_to_write.close()

else:                           # file read, get out of the else and start parsing
    pass


parser.read(CONFIG_FILE_NAME)
s1 = parser.getint('data_array', 'x')
s2 = parser.getint('data_array', 'y')
s3 = parser.getint('data_array', 'z')


shape = (s1, s2, s3)

#print(shape)
