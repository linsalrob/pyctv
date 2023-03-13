"""
Run the VMR code
"""

import os
import argparse
import sys

from pyctv_lib import parse_vmr, genbank2vmr, refseq2vmr, current_vmr, package_directory

__author__ = 'Rob Edwards'

choices = ['download', 'list', 'version']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse the current workbook and get  a list')
    parser.add_argument('command', help=f'Command to run', choices=choices)
    grp = parser.add_argument_group()
    grp.add_argument('-s', help='Print semi-colon separated taxonomy', action='store_true')
    grp.add_argument('-g', help='Print GenBank IDs and taxonomy', action='store_true')
    grp.add_argument('-r', help='Print RefSeq IDs and taxonomy', action='store_true')
    grp2 = parser.add_argument_group()
    grp2.add_argument('-f', help='Force an update, even if you have the newest file', action='store_true')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()


    if args.command == 'list':
        done = False
        if args.s:
            done = True
            for l in parse_vmr(verbose=args.v):
                print(l)
        if args.g:
            done = True
            gbk2vmr = genbank2vmr(verbose=args.v)
            for g in gbk2vmr:
                print(f"{g}: {gbk2vmr[g]}")
        if args.r:
            done = True
            rf2vmr = refseq2vmr(verbose=args.v)
            for r in rf2vmr:
                print(f"{r}: {rf2vmr[r]}")
        if not done:
            print("Please choose one (or more) of -s, -g, -r", file=sys.stderr)
            exit(2)

    if args.command == 'download':
        current_vmr(force_download=args.f, verbose=args.v)

    if args.command == 'version':
        with open(os.path.join(package_directory, "VERSION"), "r") as ver:
            l = ver.read().strip()
        print(l)