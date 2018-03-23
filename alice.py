#!/usr/bin/env python

import sys
import socket


port = 8671
ip = '127.0.0.1'

alice_key = '23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    '''sock.sendto(bytes('lookup ' + data, "utf-8"), (ip, port))
    received = str(sock.recv(1024), "utf-8")
    print('DNSLookup: ' + data + ' is ' + received)'''
