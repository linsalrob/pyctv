"""
A generic script to run some tests
"""

import argparse
from pyctv_lib import parse_vmr, genbank2vmr, refseq2vmr

__author__ = 'Rob Edwards'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse the current workbook and get  a list')
    grp = parser.add_argument_group()
    grp.add_argument('-s', help='Print semi-colon separated taxonomy', action='store_true')
    grp.add_argument('-g', help='Print GenBank IDs and taxonomy', action='store_true')
    grp.add_argument('-r', help='Print RefSeq IDs and taxonomy', action='store_true')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    if args.s:
        for l in parse_vmr(verbose=args.v):
            print(l)

    if args.g:
        gbk2vmr = genbank2vmr(verbose=args.v)
        for g in gbk2vmr:
            print(f"{g}: {gbk2vmr[g]}")

    if args.r:
        rf2vmr = refseq2vmr(verbose=args.v)
        for r in rf2vmr:
            print(f"{r}: {rf2vmr[r]}")
