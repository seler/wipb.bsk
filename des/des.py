#!/usr/bin/env python
import sys


class DES(object):

    permutations = {
        'PC1': [
            57, 49, 41, 33, 25, 17,  9,
             1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27,
            19, 11,  3, 60, 52, 44, 36,

            63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29,
            21, 13,  5, 28, 20, 12,  4
        ],
        'PC2': [
            14, 17, 11, 24,  1,  5,
             3, 28, 15,  6, 21, 10,
            23, 19, 12,  4, 26,  8,
            16,  7, 27, 20, 13,  2,

            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ],
        'IP': [
            58, 50, 42, 34, 26, 18, 10,  2,
            60, 52, 44, 36, 28, 20, 12,  4,
            62, 54, 46, 38, 30, 22, 14,  6,
            64, 56, 48, 40, 32, 24, 16,  8,
            57, 49, 41, 33, 25, 17,  9,  1,
            59, 51, 43, 35, 27, 19, 11,  3,
            61, 53, 45, 37, 29, 21, 13,  5,
            63, 55, 47, 39, 31, 23, 15,  7
        ],
        'IP1': [
            40,  8, 48, 16, 56, 24, 64, 32,
            39,  7, 47, 15, 55, 23, 63, 31,
            38,  6, 46, 14, 54, 22, 62, 30,
            37,  5, 45, 13, 53, 21, 61, 29,
            36,  4, 44, 12, 52, 20, 60, 28,
            35,  3, 43, 11, 51, 19, 59, 27,
            34,  2, 42, 10, 50, 18, 58, 26,
            33,  1, 41,  9, 49, 17, 57, 25
        ],
        'E': [
            32,  1,  2,  3,  4, 5,
             4,  5,  6,  7,  8, 9,
             8,  9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32,  1
        ],
        'P': [
            16,  7, 20, 21,
            29, 12, 28, 17,
             1, 15, 23, 26,
             5, 18, 31, 10,
             2,  8, 24, 14,
            32, 27,  3,  9,
            19, 13, 30,  6,
            22, 11,  4, 25,
        ],
    }

    left_shifts_count = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    S = [
        [
            14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
             0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
             4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
            15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
        ],
        [
            15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
             3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
             0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
            13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14, 9
        ],
        [
            10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
            13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
            13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
             1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
        ],
        [
             7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
            13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
            10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
             3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
        ],
        [
             2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
            14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
             4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
            11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
        ],
        [
            12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
            10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
             9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
             4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
        ],
        [
             4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
            13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
             1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
             6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
        ],
        [
            13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
             1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
             7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
             2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
        ]
    ]

    def __init__(self, verbose=False, proc_i=0, proc_n=0):
        self.verbose = verbose
        self.key = {}
        self.keys = {}
        self.proc_i = proc_i
        self.proc_n = proc_n

    def printf(self, msg, bits=None, n=8):
        if self.verbose:
            if bits:
                nbits = ''
                for i in range(len(bits)):
                    if not i % n and i:
                        nbits += ' '
                    nbits += bits[i]
                print msg, nbits
            else:
                print msg

    def permutate(self, p, data):
        result = ''
        for i in self.permutations[p]:
            result += data[i - 1]
        return result

    def left_shift(self, bits):
        return bits[1:] + bits[0]

    def chr2ord(self, data):
        return map(ord, data)

    def hex2ord(self, data):
        return [int(data[i] + data[i + 1], 16) for i in xrange(0, 16, 2)]

    def ord2bin(self, data):
        bits = "".join(map(lambda i: "{0:08b}".format(i), data))
        return bits

    def bin2ord(self, data):
        result = []
        for i in self.chunks(data, 8):
            result.append(int(i, 2))
        return result

    def ord2hex(self, data):
        return map(lambda i: "{0:02x}".format(i), data)

    def ord2chr(self, data):
        return "".join(map(chr, data))

    def set_key(self, s, key):
        key = key.replace(" ", "")
        key = key.replace(":", "")
        key = key.replace("-", "")
        self.key[s] = self.ord2bin(self.hex2ord(key))

    def generate_keys(self, s):
        keys = self.permutate('PC1', self.key[s])
        c = keys[:28]
        d = keys[28:]
        self.printf('CD[0]: ', c + d, 7)
        self.keys[s] = []
        for i in range(16):
            for j in range(self.left_shifts_count[i]):
                c = self.left_shift(c)
                d = self.left_shift(d)
            k = self.permutate('PC2', c + d)
            self.printf('CD[%d]: ' % (i + 1), c + d, 7)
            self.printf('KS[%d]: ' % (i + 1), k, 6)
            self.keys[s].append(k)

    def chunks(self, l, n):
        return (l[i:i + n] for i in range(0, len(l), n))

    def f(self, R, KS):
        E = self.permutate('E', R)
        self.printf('E   : ', E, 6)
        self.printf('KS  : ', KS, 6)
        B = self.xor(E, KS)
        self.printf('E xor KS: ', B, 6)
        Sbox = ''
        for c, C in enumerate(self.chunks(B, 6)):
            i, j = int(C[0] + C[-1], 2), int(C[1:-1], 2)
            Sbox += "{0:04b}".format(self.S[c][i * 16 + j])
        self.printf('Sbox: ', Sbox, 4)

        P = self.permutate('P', Sbox)
        self.printf('P   :', P)
        return P

    def xor(self, A, B):
        result = ''
        assert len(A) == len(B)
        for i in xrange(len(A)):
            result += str((int(A[i]) + int(B[i])) % 2)
        return result

    def fill(self, bytes):
        to_fill = 8 - len(bytes)
        for i in range(to_fill):
            if i == 0:
                bytes += chr(128)
            else:
                bytes += chr(0)
        return bytes

    def strip(self, bytes):
        bytes = bytes.rstrip(chr(0))
        return bytes.rstrip(chr(128))

    def encrypt(self, key, filename, key2=None):
        self.set_key('S1', key)
        self.printf('Key bits:', self.key['S1'])
        self.generate_keys('S1')
        if key2:
            self.set_key('S2', key2)
            self.generate_keys('S2')
            self.keys['S2'].reverse()

        result = ''

        input = open(filename, 'rb')
        input.seek(self.proc_i * 8)
        bytes = input.read(8)
        filled = False
        while bytes:
            enciphered = self.encrypt8bytes(bytes, 'S1')
            if key2:
                enciphered = self.encrypt8bytes(enciphered, 'S2')
                enciphered = self.encrypt8bytes(enciphered, 'S1')
            result += enciphered
            input.seek(input.tell() + self.proc_n * 8)
            bytes = input.read(8)
            if len(bytes) != 8 and not filled:
                bytes = self.fill(bytes)
                filled = True
        return result

    def encrypt8bytes(self, bytes, key='S1'):
        ords = self.chr2ord(bytes)
        bits = self.ord2bin(ords)
        self.printf('Input bits:', bits)
        bits = self.permutate('IP', bits)
        L = bits[:32]
        R = bits[32:]
        self.printf('L[0]: ', L)
        self.printf('R[0]: ', R)
        for i in range(16):
            self.printf('Round %d' % (i + 1))
            R, L = self.xor(L, self.f(R, self.keys[key][i])), R
            self.printf('L[i]:', L)
            self.printf('R[i]:', R)
        self.printf('LR[16] ', R + L)
        output = self.permutate('IP1', R + L)
        self.printf('Output ', output)
        ordout = self.bin2ord(output)
        self.printf('Output ', self.ord2hex(ordout))
        self.printf('Output ', self.ord2chr(ordout))
        return self.ord2chr(ordout)

    def decrypt(self, key, filename, key2=None):
        self.set_key('S1', key)
        self.printf('Key bits:', self.key['S1'])
        self.generate_keys('S1')
        self.keys['S1'].reverse()
        if key2:
            self.set_key('S2', key2)
            self.generate_keys('S2')

        result = ''

        input = open(filename, 'rb')
        input.seek(self.proc_i * 8)

        bytes = input.read(8)
        while bytes:
            plaintext = self.encrypt8bytes(bytes, 'S1')
            if key2:
                plaintext = self.encrypt8bytes(plaintext, 'S2')
                plaintext = self.encrypt8bytes(plaintext, 'S1')
            input.seek(input.tell() + self.proc_n * 8)
            bytes = input.read(8)
            if not bytes:
                plaintext = self.strip(plaintext)
            result += plaintext
        return result


def execute(verbose, proc_i, proc_n, encrypt, key1, key2, input):

    des = DES(verbose=args.verbose, proc_i=proc_i, proc_n=proc_n)

    if args.encrypt:
        action = des.encrypt
    else:
        action = des.decrypt

    return action(key1, input, key2)

if __name__ == "__main__":
    import argparse
    from multiprocessing import Pool
    import time

    parser = argparse.ArgumentParser(description='Encrypts/decrypts given file using DES or 3DES algorithm.')
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('--key', nargs=1)
    group1.add_argument('--keys', nargs=2, metavar='KEY')

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-e', '--encrypt', action='store_true')
    group2.add_argument('-d', '--decrypt', action='store_true')

    parser.add_argument('-v', '--verbose', action='store_true')

    parser.add_argument('-i', '--infile', required=True)
    parser.add_argument('-o', '--outfile',
                nargs='?',
                type=argparse.FileType('wb'),
                default=sys.stdout,
                help='output file to process, if not given stdout will be used')

    args = parser.parse_args()

    if args.key:
        key1 = args.key
        key2 = None
    if args.keys:
        key1, key2 = args.keys

    t1 = time.time()

    pool = Pool(processes=4)

    proc_n = 3

    proc_i = 0
    result1 = pool.apply_async(execute, [args.verbose, proc_i, proc_n, args.encrypt, key1, key2, args.infile])
    proc_i = 1
    result2 = pool.apply_async(execute, [args.verbose, proc_i, proc_n, args.encrypt, key1, key2, args.infile])
    proc_i = 2
    result3 = pool.apply_async(execute, [args.verbose, proc_i, proc_n, args.encrypt, key1, key2, args.infile])
    proc_i = 3
    result4 = pool.apply_async(execute, [args.verbose, proc_i, proc_n, args.encrypt, key1, key2, args.infile])
    output1 = result1.get()
    output2 = result2.get()
    output3 = result3.get()
    output4 = result4.get()

    print "czas:", round(time.time() - t1, 2), 'sekundy'

    while output1 or output2 or output3 or output4:
        args.outfile.write(output1[:8])
        output1 = output1[8:]
        args.outfile.write(output2[:8])
        output2 = output2[8:]
        args.outfile.write(output3[:8])
        output3 = output3[8:]
        args.outfile.write(output4[:8])
        output4 = output4[8:]

