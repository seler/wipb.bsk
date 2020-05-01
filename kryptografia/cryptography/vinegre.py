# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"


class Vinegre(object):
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
