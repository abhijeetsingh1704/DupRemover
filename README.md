# "DupRemover" - Duplicate remover
Removes duplicate sequences in multifasta file.

-------------------------

DupRemover finds duplicate sequences and keeps unique sequence while concatenating all the fasta headers together in a nucleotide or amino acid multifasta file.

## Dependencies
Biopython >= 1.78

## Install biopython (if not already installed)
pip3 install biopython

or

python3 -m pip install biopython 


## Usage
python3 DupRemover.py /path/to/input_file  /path/to/output_file
  
  ```
  python3 DupRemover.py Mixed_sequences.fasta Unique_sequences.fasta
  ```


#### LICENSE
Duplicate-remover is licensed under the
GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
