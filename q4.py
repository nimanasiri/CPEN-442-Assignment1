from binascii import crc32
import datetime

CRCPOLY = 0xEDB88320
CRCINV = 0x5B358FD3

start = datetime.datetime.now()

buf = bytearray([0,0,0,0])

# SID
x = b'227C7A616910928FF848FC022C9E0FCF'


y = crc32(x) ^ 0xFFFFFFFF
hash = crc32(x) ^ 0xFFFFFFFF

spoof = 0
for i in range(32):
    if spoof & 1 != 0:
        spoof = (spoof >> 1) ^ CRCPOLY
    else:
        spoof = spoof >> 1
    
    if y & 1 != 0:
        spoof ^= CRCINV

    y = y >> 1

spoof ^= hash

for i in range(4):
    buf[i] = (spoof >> i*8) & 0xFF
    
y = x + buf

print("Stored y in y.txt. It has the same hash as x={}".format(x))
print("The hex format of y is: {}".format(y.hex()))

f = open("y.txt", "wb")
f.write(x+buf)

print("Exec time: {}".format(datetime.datetime.now() - start))