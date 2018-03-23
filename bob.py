#!/usr/bin/env python

import sys
import socket
import random


server_address = '127.0.0.1'
server_port = 8671
server = (server_address, server_port)

bobs_key = 'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'
bobs_nonce = -1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(10)
    sock.bind(server)
    print('Listening on ' + server_address + ':' + str(server_port))

    while True:
        print('bob: waiting for request...')
        payload, client_address = sock.recvfrom(1024)

        if payload.decode('utf-8') == 'Let\'s talk':
            bobs_nonce = random.randint(1, 101)
            print('Let\'s talk received, sending ' + str(bobs_nonce) + ' as the nonce')
            sock.sendto(bytes(str(bobs_nonce), "utf-8"), client_address)
            exit()
        else:
            print(payload)
