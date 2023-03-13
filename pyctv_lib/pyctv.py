"""

"""

import os
import sys
import argparse
from pyctv_lib import parse_vmr, genbank2vmr, refseq2vmr, current_vmr, package_directory

__author__ = 'Rob Edwards'

def run():
    choices = ['download', 'list', 'version']
    parser = argparse.ArgumentParser(description='Parse the current workbook and get  a list')
    parser.add_argument('command', help=f'Command to run', choices=choices)
    grp = parser.add_argument_group()
    grp.add_argument('-s', '--semi', help='Print semi-colon separated taxonomy', action='store_true')
    grp.add_argument('-g', '--genbank', help='Print GenBank IDs and taxonomy', action='store_true')
    grp.add_argument('-r', '--refseq', help='Print RefSeq IDs and taxonomy', action='store_true')
    grp2 = parser.add_argument_group()
    grp2.add_argument('-f', '--force', help='Force an update, even if you have the newest file', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')
    args = parser.parse_args()


    if args.command == 'list':
        done = False
        if args.semi:
            done = True
            for l in parse_vmr(verbose=args.verbose):
                print(l)
        if args.genbank:
            done = True
            gbk2vmr = genbank2vmr(verbose=args.verbose)
            for g in gbk2vmr:
                print(f"{g}: {gbk2vmr[g]}")
        if args.refseq:
            done = True
            rf2vmr = refseq2vmr(verbose=args.verbose)
            for r in rf2vmr:
                print(f"{r}: {rf2vmr[r]}")
        if not done:
            print("Please choose one (or more) of -s, -g, -r", file=sys.stderr)
            exit(2)
        exit(0)

    if args.command == 'download':
        current_vmr(force_download=args.force, verbose=args.verbose)
        exit(0)

    if args.command == 'version':
        with open(os.path.join(package_directory, "VERSION"), "r") as ver:
            l = ver.read().strip()
        print(l)