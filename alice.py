#!/usr/bin/env python

import sys
import socket
import binascii
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits


port = 8671
kdc_port = 8888
ip = '127.0.0.1'

alices_key = b'23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    print('Sending "Let\'s Talk" to Bob')
    sock.sendto('Let\'s talk'.encode('utf-8'), (ip, port))
    print('Waiting for nonce from Bob')
    bobs_encrypted_nonce = sock.recv(1024)
    print('Nonce received from Bob, messaging the KDC')

    alices_nonce = getrandbits(32)
    kdc_message = str(alices_nonce).encode() + b' Alice Bob ' + bobs_encrypted_nonce
    sock.sendto(kdc_message, (ip, kdc_port))
