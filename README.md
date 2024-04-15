# fasta_unalignr

Author: Murat Buyukyoruk

        fasta_unalignr help:

This script is developed to unalign a multi sequence alignment if needed. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain 
long and many sequences.

Syntax:

        python fasta_unalignr.py -i demo.fasta

fasta_unalignr dependencies:
	Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download
	tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a multi sequence alignment fasta file.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

