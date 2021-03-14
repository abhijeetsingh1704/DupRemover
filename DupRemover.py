#!/usr/bin/env python3

# File      - DupRemover
# Modified  - Sun Mar 14 13:46:06 CET 2021
# Sign      - Abhijeet

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
input_obj = open(sys.argv[1], 'r')
output_obj = open(sys.argv[2], 'w')
# Print info
date = datetime.datetime.now()
print("[Script]\t: DupRemover")
print("[Date]\t\t: "+ date.strftime("%Y-%m-%d %H:%M:%S"))
print("[Input file]\t: "+ input_obj.name)
print("[Output file]\t: "+ output_obj.name)

# reading and parsing fasta file
uniq_seqs = defaultdict(list)
for qry in SeqIO.parse(input_obj, 'fasta'):
    # making keys and list from sequence and ids + descriptions
    uniq_seqs[str(qry.seq)].append(qry.description)
# making unique sequences
final_seq = (SeqRecord(Seq(seqi), id="|".join(accn), name='', description='') for seqi, accn in uniq_seqs.items())
# write output file
output_num = SeqIO.write(final_seq, output_obj, 'fasta')

# sequence counts
input_num = 0
for input_seqs in open(sys.argv[1], 'r'):
    if input_seqs.startswith(">"):
        input_num += 1
    
print("[input seq]\t:", input_num)
print("[Output seq]\t:", output_num)

# Number of duplicate sequences
Duplicate_num = input_num - output_num
print("[Duplicates]\t:", Duplicate_num)

# close file
input_obj.close()
output_obj.close()
# END OF SCRIPT
