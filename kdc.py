#!/usr/bin/env python

import sys
import socket


port = 8888

alice_key = '23FCE5AE61E7BFCB29AC85725E7EC77DB9DBA460EACA7458070B719CE0B1DC31'
bob_key = 'A41503A5D9E66B34FAC9F2FC9FD14CA24D728B17DE0FCC2C3676DED6A191A1F1'
session_key = 'V34UT5YH4UYDT5FG3UX5Y3J4CXYX3RYDTUC5LT3UC45TUVGJ3YU4V5HBJB4J3V5U'

if __name__ == '__main__':
    '''sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server)
    print("Listening on " + server_address + ":" + str(server_port))

    while True:
        print('DNSResolver: waiting for request...')
        payload, client_address = sock.recvfrom(1024)
        request = payload.decode("utf-8").split(' ')

        if request[0] == 'lookup':
            print('DNSResolver: Request received - ' + request[1])

            if request[1] in dns_table:
                print('DNSResolver: Responding with ' + dns_table[request[1]])
                sock.sendto(bytes(dns_table[request[1]], "utf-8"), client_address)'''
