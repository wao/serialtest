#!/usr/bin/env python3

import serial
import sys

ser = serial.Serial(port=sys.argv[1], baudrate=int(sys.argv[2]), bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

buf = bytes([i for i in range(1,255)])

total_pkt_cnt = 0

while True:
    len = ser.write(buf)
    total_pkt_cnt += 1
    print("[%016d] write packet len %d " % ( total_pkt_cnt, len ))
