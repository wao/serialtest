#!/usr/bin/env python3

import serial
import sys

ser = serial.Serial(port=sys.argv[1], baudrate=int(sys.argv[2]), bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

expect_buf = bytes([i for i in range(1,255)])

expect_offset = 0
buf_len = len(expect_buf)
total_byte = 0
error_cnt = 0

print_cnt = 0

while True:
    buf = ser.read(1024)
    total_byte += len(buf)
    #print( "recv new buf, total %d error %d" % ( total_byte, error_cnt ) )
    print_cnt += len(buf)
    if print_cnt > 100000:
        print_cnt = 0
        print( "total %d error %d" % ( total_byte, error_cnt ) )

    i = 0
    while i < len(buf):
        if buf[i] == 0:
            print( "skip 0" )
            i += 1
            continue

        if buf[i] != expect_buf[expect_offset]:
            print( "expect %d, but got %d" % ( expect_buf[expect_offset], buf[i] ) )
            if expect_offset < buf[i]-1:
                error_cnt += buf[i] -1 - expect_offset
            else:
                error_cnt += 255 + buf[i] -1 - expect_offset 
            print( "total %d error %d" % ( total_byte, error_cnt ) )
            expect_offset = buf[i]-1
        i += 1
        expect_offset += 1
        if expect_offset >= buf_len:
            expect_offset = 0

