#!/usr/bin/env python3

# File - DupRemover
# Modified - Mon Mar  8 13:55:17 CET 2021
# Sign - Abhijeet


import sys
import datetime
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from collections import defaultdict

# user options
input = open (sys.argv[1], 'r')
out = open (sys.argv[2], 'w')

# Print info
date = datetime.datetime.now()
print("\n"+"[Script]       : DupRemover")
print("[Date]         : "+ date.strftime("%Y-%m-%d %H:%M:%S"))
print("[Input file]   : "+ sys.argv[1])
print("[Output file]  : "+ sys.argv[2]+"\n")


# reading and parsing fasta file
uniq_seqs = defaultdict(list)

for qry in SeqIO.parse(input, 'fasta'):

    # making keys and list from sequence and ids + descriptions
    uniq_seqs[str(qry.seq)].append(qry.description)

# making unique sequences
final_seq = (SeqRecord(Seq(seqi, IUPAC.protein), id="|".join(accn), name='', description='') for seqi, accn in uniq_seqs.items())

# write file
SeqIO.write(final_seq, out, 'fasta')

# close file
input.close()
out.close()
