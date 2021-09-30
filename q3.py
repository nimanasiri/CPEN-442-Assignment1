from binascii import crc32
import os
import datetime

start = datetime.datetime.now()

input_map = {}

while True:
    x = bytes(os.urandom(32).hex(), 'ascii')

    hash = crc32(x) & 0xffffffff # from documentation

    if hash in input_map:
        print("found a collision: x = {}, y = {}".format(x, input_map[hash]))
        break
    else:
        input_map[hash] = x

print("Exec time: {}".format(datetime.datetime.now() - start))