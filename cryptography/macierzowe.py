# -*- coding: utf-8 -*-


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
        x = len(self.text) % len(self.key)
        if x:
            self.text += '_' * (len(self.key) - x)

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

        self.przerob_klucz()
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

    def przerob_klucz(self):
        new_key = [None for x in range(len(self.key))]
        for i in range(len(self.key)):
            new_key[self.key[i] - 1] = i + 1
        self.key = new_key

    def decrypt(self, string, key):
        self.clear()
        self.setText(string)
        self.setKey(key)
        if not self.sprawdzKlucz():
            return "klucz nieciagly"
        else:
            self.przerob_klucz()
            return self.encrypted().rstrip('_')

    def clear(self):
        self.text = ""
        self.key = []
        self.sortedKey = []
        self.stringArray = []


class MacierzoweB(object):
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        self.matrix = []
        for k in key:
            self.matrix.append([k, []])

        for i, c in enumerate(plaintext):
            self.matrix[i % len(key)][1].append(c)

        self.matrix = sorted(self.matrix, key=lambda x: x[0])

        ciphertext = ''

        for a in self.matrix:
            for b in a[1]:
                ciphertext += b

        return ciphertext

    def decrypt(self, ciphertext, key):
        matrix = []
        for k in key:
            matrix.append([k, []])

        matrix.sort()

        rows = len(ciphertext) / len(key)
        rest = len(ciphertext) % len(key)

        k = 0
        for i in range(len(key)):
            for j in range(rows + bool(rest)):
                matrix[i][1].append(ciphertext[k])
                k += 1
            if rest:
                rest -= 1

        matrix2 = []
        for k in key:
            matrix2.append([k, []])

        for a in matrix:
            for i, b in enumerate(matrix2):
                if a[0] == b[0] and not b[1]:
                    matrix2[i] = a
                    break

        matrix3 = map(lambda a: a[1], matrix2)

        matrix4 = map(None, *matrix3)

        plaintext = ''

        for i in matrix4:
            for j in i:
                try:
                    plaintext += j
                except TypeError:
                    pass

        return plaintext


class MacierzoweC(object):
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        key = map(None, key)
        sorted_key = sorted(key[:])
        new_key = key[:]
        for i in range(len(key)):
            index = key.index(sorted_key[i])
            key[index] = None
            new_key[i] = index

        key = new_key

        matrix = []
        for i, c in enumerate(plaintext):

            # petla wyliczajaca pozycje
            for j in range(len(key)):
                position = j
                try:
                    if key[j] >= len(matrix[j]):
                        break
                except IndexError:
                    break
            try:
                matrix[position]
            except IndexError:
                matrix.append([])
            finally:
                matrix[position].append(c)

        from pprint import pprint
        pprint(matrix)

        matrix = map(None, *matrix)

        matrix2 = matrix[:]
        for i, j in enumerate(new_key):
            try:
                matrix2[i] = matrix[j]
            except IndexError:
                pass

        ciphertext = ''

        for a in matrix2:
            for b in a:
                if b is not None:
                    ciphertext += b

        return ciphertext

    def decrypt(self, ciphertext, key):
        key = map(None, key)
        sorted_key = sorted(key[:])
        new_key = key[:]
        for i in range(len(key)):
            index = key.index(sorted_key[i])
            key[index] = None
            new_key[i] = index

        key = new_key

        matrix = []
        for i, c in enumerate(ciphertext):
            # petla wyliczajaca pozycje
            for j in range(len(key)):
                position = j
                try:
                    if key[j] >= len(matrix[j]):
                        break
                except IndexError:
                    break
            try:
                matrix[position]
            except IndexError:
                matrix.append([])
            finally:
                matrix[position].append('')

        matrix2 = map(None, *matrix)
        matrix3 = matrix[:]
        for i, j in enumerate(new_key):
            try:
                matrix3[i] = list(matrix2[j])
            except IndexError:
                pass

        position = 0
        for i, a in enumerate(matrix3):
            for j, b in enumerate(a):
                if isinstance(b, str):
                    try:
                        c = ciphertext[position]
                    except IndexError:
                        c = ''
                    matrix3[i][j] = c
                    position += 1

        matrix4 = [None for x in range(max(len(matrix3), len(key)))]

        for i in range(len(matrix4)):
            try:
                matrix4[key[i]] = matrix3[i]
            except IndexError:
                matrix4[key[i]] = []

        import pdb
        pdb.set_trace()

        matrix5 = zip(*matrix4)

        plaintext = ''

        for i in matrix5:
            for j in i:
                try:
                    plaintext += j
                except TypeError:
                    pass

        if len(ciphertext) > len(plaintext):
            plaintext += ciphertext[len(plaintext):]

        return plaintext


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('text')
    parser.add_argument('key')

    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('-ma', '--MacierzoweA',
                dest='ma',
                action='store_true',
                help='Encode/decode using przestawienia macierzowe A')
    group1.add_argument('-mb', '--MacierzoweB',
                dest='mb',
                action='store_true',
                help='Encode/decode using przestawienia macierzowe B')
    group1.add_argument('-mc', '--MacierzoweC',
                dest='mc',
                action='store_true',
                help='Encode/decode using przestawienia macierzowe C')

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-e', '--encrypt',
                dest='encrypt',
                action='store_true',
                help='encrypt')
    group2.add_argument('-d', '--decrypt',
                dest='decrypt',
                action='store_true',
                help='decrypt')

    args = parser.parse_args()

    if args.ma:
        crypt_class = MacierzoweA()
    elif args.mb:
        crypt_class = MacierzoweB()
    elif args.mc:
        crypt_class = MacierzoweC()

    if args.encrypt:
        result = crypt_class.encrypt(args.text, args.key)
    elif args.decrypt:
        result = crypt_class.decrypt(args.text, args.key)
    print(result)
