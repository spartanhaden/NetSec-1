#!/usr/bin/env python

import socket
import binascii
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits

server_address = '127.0.0.1'
server_port = 8671

bobs_key = b'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'


def encrypt(key, data):
    # Setup the cipher to encrypt the data
    cipher = AES.new(binascii.unhexlify(key), AES.MODE_SIV)

    # Encrypt the data
    ciphertext, digest = cipher.encrypt_and_digest(data)

    # Convert to ascii to comply with assignment description
    ascii_ciphertext = binascii.hexlify(ciphertext)
    ascii_digest = binascii.hexlify(digest)

    # Concatenate the ciphertext and digest
    return ascii_ciphertext + b'-' + ascii_digest


def decrypt(key, data):
    # Setup the cipher to decrypt the data
    cipher = AES.new(binascii.unhexlify(key), AES.MODE_SIV)

    # Split the ciphertext from the digest
    ascii_ciphertext, ascii_digest = data.split(b'-')

    # Decrypt the message
    return cipher.decrypt_and_verify(binascii.unhexlify(ascii_ciphertext), binascii.unhexlify(ascii_digest))


if __name__ == '__main__':
    # Setup socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    sock.bind((server_address, server_port))
    print('Listening on ' + server_address + ':' + str(server_port))

    while True:
        # Waits for message from Alice
        print('Bob: waiting for request...')
        payload, client_address = sock.recvfrom(4096)

        # Receives first message from Alice and responds with an encrypted nonce
        if payload.decode() == 'Let\'s talk':
            bobs_nonce = getrandbits(32)
            print('Let\'s talk received, sending ' + str(bobs_nonce) + ' as the nonce')
            message = encrypt(bobs_key, str(bobs_nonce).encode())
            sock.sendto(message, client_address)
            #exit()
        else:
            print(payload)
