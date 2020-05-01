# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"


class Vigenere(object):
    def __init__(self):
        self.start = ord('A')
        self.length = 26

    def troll(self, string, key):
        if len(string) != len(key):
            raise Exception("zla dlugosc")

        string, key = string.upper(), key.upper()

        for i in range(len(key)):
            for x in (string, key):
                for c in x:
                    if ord(c) < self.start or ord(c) > self.start + self.length:
                        raise Exception('niedozwolony znak "%s"' % c)
        return string, key

    def encrypt(self, string, key):
        string, key = self.troll(string, key)
        return ''.join([chr((ord(string[i]) + ord(key[i]) + (2 * self.start)) % self.length + self.start) for i in range(len(string))])

    def decrypt(self, string, key):
        string, key = self.troll(string, key)
        return ''.join([chr((ord(string[i]) - ord(key[i])) % self.length + self.start) for i in range(len(string))])


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import argparse

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('text')
    parser.add_argument('key')

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

    crypt = Vigenere()

    if args.encrypt:
        result = crypt.encrypt(args.text, args.key)
    elif args.decrypt:
        result = crypt.decrypt(args.text, args.key)
    print(result)
