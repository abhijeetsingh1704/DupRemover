#!/usr/bin/env python3

# File - DupRemover
# Modified - Sun Mar 14 11:40:50 CET 2021
# Sign - Abhijeet

import sys
import datetime
import subprocess
from collections import defaultdict
#
try:
    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
except ImportError:
    print("Biopython missing, attempting to install...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "biopython>=1.78"])
    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord

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
final_seq = (SeqRecord(Seq(seqi), id="|".join(accn), name='', description='') for seqi, accn in uniq_seqs.items())
# write file
SeqIO.write(final_seq, out, 'fasta')
# close file
input.close()
out.close()
# END OF SCRIPT
