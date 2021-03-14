# "DupRemover" - Duplicate remover
Removes duplicate sequences in multifasta file.

-------------------------

DupRemover finds duplicate sequences and keeps unique sequence while concatenating all the fasta headers together in a nucleotide or amino acid multifasta file.

## Dependencies
Biopython >=1.78

DupRemover can install biopython>=1.78 package, if biopython is not installed.

Please upgrade to biopython>=1.78 if older version is installed


## Usage
python3 DupRemover.py /path/to/input_file  /path/to/output_file
  
  ```
  python3 DupRemover.py Mixed_sequences.fasta Unique_sequences.fasta
  ```
example output
```
[Script]        : DupRemover
[Date]          : 2021-03-14 13:50:03
[Input file]    : Mixed_sequences.fasta
[Output file]   : Unique_sequences.fasta
[input seq]     : 30
[Output seq]    : 5
[Duplicates]    : 25
```

#### Citation
If you use DupRemover, please cite as:

Singh, Abhijeet. 2020. DupRemover: A Simple Program to Remove Duplicate Sequences from Multi-Fasta File. 
GitHub, DOI: 10.13140/RG.2.2.23842.86724. https://github.com/abhijeetsingh1704/Duplicate-remover.


#### LICENSE
Duplicate-remover is licensed under the
GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
