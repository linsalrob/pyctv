"""
Add a taxonomy ID column to the VMR data
"""

import os
import sys
import argparse
from pyctv_lib import parse_vmr, excel_columns

__author__ = 'Rob Edwards'





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-g', help='tuple with [GenBank ID, taxid]')
    parser.add_argument('-r', help='tuple with [RefSeq ID, taxid]')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    if not (args.g and args.r):
        print("Please use either -g or -r or both. Use -h for help", file=sys.stderr)
        sys.exit(2)

    genbank_tax = {}
    if args.g:
        with open(args.g, 'r') as fin:
            for l in fin:
                p = l.strip().split("\t")
                if len(p) < 2:
                    continue
                genbank_tax[p[0]] = p[1]


    refseq_tax = {}
    if args.r:
        with open(args.r, 'r') as fin:
            for l in fin:
                p = l.strip().split("\t")
                if len(p) < 2:
                    continue
                refseq_tax[p[0]] = p[1]

    
    cols = excel_columns()
    print("Error", end="\t", file=sys.stderr)
    for o in cols:
        print(o, end="\t", file=sys.stderr)
        print(o, end="\t")
    print("Taxonomy ID")
    print("GenBank\tRefSeq", file=sys.stderr)


    for vmr in parse_vmr():
        stderr = None  # if we set this to a value, print to STDERR 
        gbk_taxid = set()
        gbk_taxfrom = ""
        for g in vmr.genbank_ids:
            if g in genbank_tax:
                gbk_taxid.add(genbank_tax[g])
                gbk_taxfrom += f"{g}:{genbank_tax[g]}; "

        ref_taxid = set()
        ref_taxfrom = ""
        for r in vmr.refseq_ids:
            if r in refseq_tax:
                ref_taxid.add(refseq_tax[r])
                ref_taxfrom += f"{r}:{refseq_tax[r]}; "

        if len(gbk_taxid) > 1:
            # print(f"Found more than one genbank taxid: {gbk_taxid} for {vmr} : {gbk_taxfrom}", file=sys.stderr)
            stderr = "Multiple GenBank TaxIDs"
            gbk_tid = "; ".join(gbk_taxid)
        elif gbk_taxid:
            gbk_tid = gbk_taxid.pop()
        else:
            gbk_tid = ""

        if len(ref_taxid) > 1:
            # print(f"Found more than one refseq taxid: {ref_taxid} for {vmr} : {ref_taxfrom}", file=sys.stderr)
            if stderr:
                stderr = "Multiple GenBank + RefSeq taxids"
            else:
                stderr = "Multiple RefSeq taxids"
            ref_tid = "; ".join(ref_taxid)
        elif ref_taxid:
            ref_tid = ref_taxid.pop()
        else:
            ref_tid = ""

        if ref_tid and not gbk_tid:
            gbk_tid = ref_tid
        if gbk_tid and not ref_tid:
            ref_tid = gbk_tid

        if gbk_tid != ref_tid:
            if stderr:
                stderr += " and the taxonomy IDs do not match"
            else:
                stderr = "GenBank and RefSeq taxids are different"


        if stderr:
            print(stderr, end="\t", file=sys.stderr)
            for o in cols:
                print(vmr.get_attribute(cols[o]), end="\t", file=sys.stderr)
            print(f"{gbk_taxfrom}\t{ref_taxfrom}", file=sys.stderr)
        else:
            for o in cols:
                print(vmr.get_attribute(cols[o]), end="\t")
            print(gbk_tid)


    

