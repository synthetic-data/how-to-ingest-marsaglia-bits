# How to read Marsaglia bit on Linux in python

file_to_read = open('/media/alxfed/toca/bits.01', mode="rb")
a = file_to_read.read()
out = file_to_read.close()

print(int(a[3]))
