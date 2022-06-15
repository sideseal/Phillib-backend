#!/usr/bin/env python3

###################
#  python 3.7.10  #
###################

import sys


def print_process(text, n):
    print(text)
    for _ in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")
