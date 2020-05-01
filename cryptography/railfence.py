# -*- coding: utf-8 -*-

__author__ = "Rafał Selewońko <rafal@selewonko.com>"


class RailFence(object):

    def encrypt(self, string, rail):
        """
        >>> rf = RailFence()
        >>> rf.encrypt("Ala ma kota", 3)
        'Amol akta a'
        >>>
        """
        railfence = ['' for x in range(rail)]
        number = 0
        increment = 1
        for char in string:
            if number + increment == rail:
                increment = -1
            elif number + increment == -1:
                increment = 1

            railfence[number] = railfence[number] + char
            number += increment

        return ''.join(railfence)

    def decrypt(self, string, rail):
        """
        >>> rf = RailFence()
        >>> rf.decrypt("Amol akta a", 3)
        'Ala ma kota'
        >>>
        """
        length = len(string)
        railfence = [[] for x in range(rail)]

        number = 0
        increment = 1
        for i in range(length):
            if number + increment == rail:
                increment = -1
            elif number + increment == -1:
                increment = 1
            railfence[number].append(i)
            number += increment

        counter = 0
        buffer = [None for x in range(length)]
        for i in range(rail):
            for j in range(len(railfence[i])):
                buffer[railfence[i][j]] = string[counter]
                counter += 1

        return ''.join(buffer)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import argparse

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('text')
    parser.add_argument('key', type=int)

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

    crypt = RailFence()

    if args.encrypt:
        result = crypt.encrypt(args.text, args.key)
    elif args.decrypt:
        result = crypt.decrypt(args.text, args.key)
    print(result)
