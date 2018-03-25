#!/usr/bin/env python

import sys
import socket
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits
import base64


server_address = '127.0.0.1'
server_port = 8671
server = (server_address, server_port)

bobs_key = b'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'
bobs_nonce = -1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    sock.bind(server)
    print('Listening on ' + server_address + ':' + str(server_port))

    while True:
        #Waits for message from Alice
        bob_cipher = AES.new(bobs_key, AES.MODE_SIV)
        print('bob: waiting for request...')
        payload, client_address = sock.recvfrom(1024)

        # Receives first messge from Alice and responds with an encrypted nonce
        if payload.decode('utf-8') == 'Let\'s talk':
            bobs_nonce = getrandbits(32)
            print('Let\'s talk received, sending ' + str(bobs_nonce) + ' as the nonce')
            ciphertext, tag = bob_cipher.encrypt_and_digest(str(bobs_nonce).encode('utf-8'))
            sock.sendto(ciphertext + b'_' + tag, client_address)
            exit()
        else:
            print(payload)
