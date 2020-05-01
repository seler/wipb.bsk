# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"


class MacierzoweA(object):
    text = ''
    key = []
    sortedKey = []
    stringArray = []

    def __init__(self):
        pass

    def setText(self, s):
        self.text = s

    def setKey(self, s):
        self.key = []
        nums = s.split("-")
        for n in nums:
            self.key.append(int(n))
        self.sortedKey = self.key[:]
        self.sortedKey.sort()

    def reverseKey(self):
        self.key.reverse()

    def czyCiagla(self):
        ret = True
        for i in range(self.maxKey()):
            if i + 1 not in self.key:
                ret = False
        return ret

    def sprawdzKlucz(self):
        ret = self.czyCiagla()

        for i in range(len(self.sortedKey)):
            if i == 0:
                tmp = self.sortedKey[i]
            if i > 0 and i < len(self.sortedKey) - 1:
                tmp = self.sortedKey[i]
                if tmp == self.sortedKey[i + 1]:
                    ret = False
        return ret

    def maxKey(self):
        return max(self.key)

    def countRows(self):
        ret = len(self.text) / self.maxKey()
        if len(self.text) % self.maxKey() > 0:
            ret += 1
        return ret

    def makeArray(self):
        i = 1
        max = self.maxKey()
        while len(self.stringArray) != self.countRows():
            first = i * max - max
            second = i * max
            if second > len(self.text):
                second = len(self.text)
            self.stringArray.append(self.text[first:second])
            i += 1

    def encrypted(self):
        self.makeArray()
        ret = ""
        for s in self.stringArray:
            for i in self.key:
                if len(s) > i - 1:
                    ret += s[i - 1]
        return ret

    def decrypted(self):
        self.makeArray()
        ret = ''

        self.reverseKey()
        for s in self.stringArray:
            licznik = 0
            m = len(s)
            for i in self.key:
                if licznik < m:
                    j = i - 1
                    while (j >= m):
                        j -= 1
                    ret += s[j]
                    licznik += 1
        return ret

    def encrypt(self, string, key):
        self.clear()
        self.setText(string)
        self.setKey(key)
        if not self.sprawdzKlucz():
            return "klucz nieciagly"
        else:
            return self.encrypted()

    def decrypt(self, string, key):
        self.clear()
        self.setText(string)
        self.setKey(key)
        if not self.sprawdzKlucz():
            return "klucz nieciagly"
        else:
            return self.decrypted()

    def clear(self):
        self.text = ""
        self.key = []
        self.sortedKey = []
        self.stringArray = []
