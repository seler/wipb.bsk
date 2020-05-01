#!/usr/bin/env python

if __name__ == "__main__":
    import sys
    import argparse
    from des import DES

    parser = argparse.ArgumentParser(description='Encrypts/decrypts given file using DES or 3DES algorithm.')
    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument('--key', nargs=1)
    group1.add_argument('--keys', nargs=2, metavar='KEY')

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-e', '--encrypt', action='store_true')
    group2.add_argument('-d', '--decrypt', action='store_true')

    parser.add_argument('-v', '--verbose', action='store_true')

    parser.add_argument('-i', '--infile',
                nargs='?',
                type=argparse.FileType('rb'),
                default=sys.stdin,
                help='input file to process, if not given stdin will be used')
    parser.add_argument('-o', '--outfile',
                nargs='?',
                type=argparse.FileType('wb'),
                default=sys.stdout,
                help='output file to process, if not given stdout will be used')

    args = parser.parse_args()

    des = DES(verbose=args.verbose)

    if args.encrypt:
        action = des.encrypt
    elif args.decrypt:
        action = des.decrypt

    if args.key:
        key1 = args.key
        key2 = None
    if args.keys:
        key1, key2 = args.keys

    action(key1, args.infile, args.outfile, key2)
