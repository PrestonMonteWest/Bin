#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    path = sys.argv[1]
    days = sys.argv[2]
else:
    print('Usage: {} [dir] [days]'.format(sys.argv[0]))
    exit(1)

import os, time

template = "{}: '{}'"

try:
    files = os.listdir(path)
    days = int(days)
except (NotADirectoryError, FileNotFoundError) as err:
    print(template.format(err.strerror, err.filename))
    exit(1)
except ValueError:
    print("Not an integer: '{}'".format(days))
    exit(1)

if days > 0:
    seconds = days * 24 * 60 * 60
else:
    seconds = 0

for f in files:
    ab_path = os.path.join(path, f)

    try:
        info = os.lstat(ab_path)
    except FileNotFoundError:
        continue

    difference = time.time() - info.st_atime

    if difference >= seconds:
        try:
            os.unlink(ab_path)
        except OSError as err:
            print(template.format(err.strerror, err.filename))
        except FileNotFoundError:
            pass
