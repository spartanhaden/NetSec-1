#!/usr/bin/env python

import sys
import socket
from Crypto.Cipher import AES


port = 8671
kdc_port = 8888
ip = '127.0.0.1'

alices_key = '23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'
bobs_key = b'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'
bobs_nonce = -1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    print('Sending "Let\'s Talk" to Bob')
    sock.sendto('Let\'s talk'.encode('utf-8'), (ip, port))
    print('Waiting for nonce from Bob')
    payload = sock.recv(1024)
    split_payload = payload.split(b'_')
    ciphertext = split_payload[0]
    tag = split_payload[1]
    bob_cipher = AES.new(bobs_key, AES.MODE_SIV)
    bobs_nonce = bob_cipher.decrypt_and_verify(ciphertext, tag)
    print('Nonce received from bob is ' + str(bobs_nonce))

    alices_nonce = getrandbits(32)
    kdc_message = str(bobs_nonce).encode('utf-8') + b'_'
    kdc_message += b'Alice' + b'_'
    kdc_message += b'Bob' + b'_'
    kdc_message += ciphertext + b'_' + tag
    sock.sendto(kdc_message, (ip, kdc_port))
