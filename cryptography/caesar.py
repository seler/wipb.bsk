# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"

from fractions import gcd

universe = 'abcdefghijklmnopqrstu'


def ord(c):
    return universe.index(c)


def chr(i):
    return universe[i]


def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)


def totient(n):
    tot, pos = 0, n - 1
    while pos > 0:
        if gcd(pos, n) == 1:
            tot += 1
        pos -= 1
    return tot


class Caesar(object):
    def __init__(self):
        self.start = ord('a')
        self.length = len(universe)
        self.fi = totient(self.length)

    def troll(self, string, k0, k1):
        k0, k1 = k0 % self.length, k1 % self.length

        if lcm(k0, k1) != k0 * k1:
            raise Exception('k0 i k1 nie sa wzglednie pierwsze')

        for i in range(len(string)):
            for x in (string,):
                for c in x:
                    if ord(c) < self.start or ord(c) > self.start + self.length:
                        raise Exception('niedozwolony znak "%s"' % c)
        return string, k0, k1

    def encrypt(self, string, k0, k1=1):
        string, k0, k1 = self.troll(string, k0, k1)
        return ''.join([chr((((ord(string[i])) * k1) + k0) % self.length) for i in range(len(string))])

    def decrypt(self, string, k0, k1=1):
        string, k0, k1 = self.troll(string, k0, k1)
        chars = []
        for i in range(len(string)):
            chars.append(chr(((ord(string[i]) + (self.length - k0)) * int(pow(k1, self.fi - 1))) % self.length))
        return ''.join(chars)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import argparse

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('text')
    parser.add_argument('k0', type=int)
    parser.add_argument('k1', nargs="?", type=int, default=1)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt',
                dest='encrypt',
                action='store_true',
                help='encrypt')
    group.add_argument('-d', '--decrypt',
                dest='decrypt',
                action='store_true',
                help='decrypt')

    args = parser.parse_args()

    crypt = Caesar()

    if args.encrypt:
        result = crypt.encrypt(args.text, args.k0, args.k1)
    elif args.decrypt:
        result = crypt.decrypt(args.text, args.k0, args.k1)
    print(result)
