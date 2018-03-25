#!/usr/bin/env python

import sys
import socket
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits


server_address = '127.0.0.1'
server_port = 8888

alices_key = b'23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'
bobs_key = b'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'


def create_ticket(bobs_encrypted_nonce):
    pass


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    sock.bind((server_address, server_port))
    print('Listening on ' + server_address + ':' + str(server_port))

    while True:
        # Waits for a message from Alice
        print('KDC: waiting for request...')
        payload, client_address = sock.recvfrom(1024)

        split_payload = payload.split(b' ')
        if len(split_payload) != 4:
            print("nope")
            continue
        alices_nonce = split_payload[0]
        bobs_encrypted_nonce = split_payload[3]

        if split_payload[1] == b'Alice' and split_payload[2] == b'Bob':
            print("Message from Alice received, sending response")

            #bob_cipher = AES.new(bobs_key, AES.MODE_SIV)
            #bobs_nonce = bob_cipher.decrypt_and_verify(ciphertext, tag)
            #print('Nonce received from bob is ' + str(bobs_nonce))
