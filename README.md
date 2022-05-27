# "DupRemover" - Duplicate remover
### version 1.0.3
Removes duplicate sequences in multifasta file.

-------------------------

DupRemover finds duplicate sequences and keeps unique sequence while concatenating all the fasta headers together in a nucleotide or amino acid multifasta file.

## Dependencies
Biopython >=1.78

DupRemover can install biopython>=1.78 package, if biopython is not installed.

Please upgrade to biopython>=1.78 if older version is installed

## Help
```
python3 DupRemover.py -h
```
```
usage: DupRemover.py [-h] -i INPUT [-o OUTPUT] [-v Y/y or N/n] [-V]

Removes duplicate sequences in multifasta file, and append fasta header to unique sequence

Citation: Singh, Abhijeet. 2020. DupRemover: A Simple Program to Remove Duplicate Sequences from Multi-Fasta File
GitHub: https://github.com/abhijeetsingh1704/DupRemover; DOI: 10.13140/RG.2.2.23842.86724.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input fasta file
  -o OUTPUT, --output OUTPUT
                        output fasta file (default: Uniq_<input_fasta_file>)
  -v Y/y or N/n, --verbose Y/y or N/n
                        print progress to the terminal (default: verbose)
  -V, --version         show program's version number and exit
```
  

## Usage
python3 DupRemover.py /path/to/input_file  /path/to/output_file
  
  ```
  python3 DupRemover.py -i Mixed_sequences.fasta -o Unique_sequences.fasta
  ```
example output
```
[Program]       : DupRemover
[Date]          : 2021-03-27 14:40:21
[Input file]    : Mixed_sequences.fasta
[Output file]   : Unique_sequences.fasta
-------------------------
AHI13756.1 FthFS, partial [uncultured Arthrobacter sp.] =|= AHI13756.1 FthFS, partial [uncultured Arthrobacter sp.] =|= AHI13756.1 FthFS, partial [uncultured Arthrobacter sp.]
LRNIVIGLGGPTEGVPREAGFEITVASEVMAVFCLATGLEDLRTRLGRMTIGYTYDKKPVTVDDLGAAGAMTTLLKDAIKPNLVQTIGGTPAFIHGGPFANIAHGCNSAIATNTARSLAEVVVTEAGFGADLGAEKFMDIKARYAGCDPSAVVIVATIRALKMHGGVAKDQLKGENVQAVRDGMVNLARHASNVRKFGIHPVIAVNKFATDTADELAVVTEWAAENNIECAVADVWGQGGAGAGDLAAAVLRAIEAPSDFAPLYELEKPVEEKILTVVKEIYGGTEVDYTPAAKRVLEQIHANGWDNLPV

AHI13755.1 FthFS, partial [uncultured bacterium]
LGIDPRRITFRRVMDMNDRSLRHIVVGLGGPGQGTVREDGFDITVASEIMAVFCLATDIEDLTARLARITVGYTWDRRPVTVADLKVEGALALLLKDALKPNLVQTIAGTPALVHGGPFANIAHGCNSVIATTLGRDLADVVVTEAGFGADLGAEKYMDITSRVADVAPDAVVVVATIRALKMHGGVPRERLDEPNLAGLEAGTANLQRHVRNLGKFGFSPVVAINRFTTDTAEEIEWLLHWCSEEGVDAAVADVWAQGGGGPGGDDLAAKVLAALKRNVEFKPLYPLQMGVAEKIRVVVREIYGADDVEFSVPALRRLEEIEANGWDSVPV

AHI13754.1 FthFS, partial [uncultured bacterium]
ITSSHNLLSALVDNHIHWGGEPKLDAVRTSWRRVMDMNDRSLRNIVSGLGGPGNGSPSETGFDITVASEVMAILCLATDAEDLEARLSRIIVGYTREKKAVTAADIKATGAMMALLRDAMLPNLVQTLENNPCLVHGGPFANIAHGCNSVIATRAALKMANYVVTEAGFGADLGAEKFLNIKCRQAGLA

-------------------------
[input seq]     : 5
[Output seq]    : 3
[Duplicates]    : 2
```

#### Citation
If you use DupRemover, please cite as:

Singh A. DupRemover: a simple program to remove duplicate sequences from multi-fasta file. ResearchGate 2020. https://doi.org/10.13140/RG.2.2.23842.86724; Available at https://github.com/abhijeetsingh1704/Duplicate-remover


#### LICENSE
Duplicate-remover is licensed under the
GNU General Public License v3.0
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
