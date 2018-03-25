#!/usr/bin/env python

import socket
import binascii
from Crypto.Cipher import AES
from Crypto.Random.random import getrandbits


port = 8671
kdc_port = 8888
ip = '127.0.0.1'
bob_server = (ip, port)

alices_key = b'23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'


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

    # Send initial message to Bob
    print('Sending "Let\'s Talk" to Bob')
    sock.sendto('Let\'s talk'.encode(), bob_server)

    # Receive message back from Bob
    print('Waiting for nonce from Bob')
    bobs_encrypted_nonce = sock.recv(4096)
    print('Nonce received from Bob, messaging the KDC')

    alices_nonce = getrandbits(32)
    kdc_message = str(alices_nonce).encode() + b' Alice Bob ' + bobs_encrypted_nonce
    sock.sendto(kdc_message, (ip, kdc_port))

    kdc_response = sock.recv(4096)
    decrypted_kdc = decrypt(alices_key, kdc_response)

    kdc_split = decrypted_kdc.split()

    print(kdc_split)

    nonce2 = getrandbits(32)

    encrypted_nonce2 = encrypt(kdc_split[2], str(nonce2).encode())

    sock.sendto(kdc_split[3] + encrypted_nonce2, bob_server)

    # bobs_nonce = bob_cipher.decrypt_and_verify(ciphertext, tag)
    # print('Nonce received from bob is ' + str(bobs_nonce))
