#!/usr/bin/env python

import sys
import socket


port = 8671
ip = '127.0.0.1'

alices_key = '23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'
bobs_nonce = -1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    print('Sending \'Let\'s Talk\' to Bob')
    sock.sendto(bytes('Let\'s talk', "utf-8"), (ip, port))
    print('Waiting for nonce from Bob')
    bobs_nonce = int(sock.recv(1024))
    print('Nonce received from bob is ' + str(bobs_nonce))
