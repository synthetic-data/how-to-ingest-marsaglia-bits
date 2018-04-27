# How to read Marsaglia bit on Linux in python

file_to_read = open('/media/alxfed/toca/bits.42', mode="rb")
a = file_to_read.read(100)
out = file_to_read.close()

printable_bytes = [int(x) for x in a]
# or printable_bytes = [int(x) for x in a if x < 10]

print(printable_bytes[0:9])

# same numbers as in R example