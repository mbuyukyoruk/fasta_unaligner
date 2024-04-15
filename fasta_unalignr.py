import argparse
import sys
import os
import subprocess
import re
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python fasta_unalignr.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

      	Author: Murat Buyukyoruk

        fasta_unalignr help:

This script is developed to unalign a multi sequence alignment if needed. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

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

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a alinged fasta file.\n')

results = parser.parse_args()
filename = results.filename

out = filename.split('.')[0] + "_unaligned." + filename.split('.')[1]

os.system('> ' + out)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length), desc='Reading...') as pbar:
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        f = open(out, 'a')
        sys.stdout = f
        print('>' + record.description)
        seq_cleaned = re.sub("-", "", str(record.seq))
        print(re.sub("(.{60})", "\\1\n", str(seq_cleaned), 0, re.DOTALL))

