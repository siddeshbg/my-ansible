#!/usr/bin/env python3
from datetime import datetime
import time
from argparse import ArgumentParser

class Simulator:
    def __init__(self, count):
        self.count = count

    def loop(self):
        f = open('log.txt', 'w')
        for i in range(self.count):
            print(datetime.now())
            f.write("%s\n" % str(datetime.now()))
            time.sleep(5)


def main():
    arg_parser = ArgumentParser(description="Build Simulator Script")
    arg_parser.add_argument("-c", "--count", help='iteration count')
    args = arg_parser.parse_args()

    if not args.count:
        count = 10
    else:
        count = args.count

    s = Simulator(int(count))
    s.loop()


if __name__ == '__main__':
    main()