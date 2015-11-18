Ten Minute Plan for phage DNA parsing program:

Nico Crudele

The goal of this project is to be able to list the spacer sequences is a DNA strand, by parsing apart the repeats in a genome that contains a CRISPR array. 
 Where the CRISPR array is on the bacteria’s genome, the DNA sequence at this point follows a pattern, which is CRISPR, phage spacer, CRISPR, phage spacer, etc.


What it needs to do:
As the repetitive sequences are the same sequence in a given CRISPR system, my program needs to be able to list all of the spacer sequences individually,
 recognizing their beginning point at the end of the previous repetitive sequence, and their end point by recognizing the beginning of a repetitive sequence.

Attempts so far:
I have made regular expressions which will count the number of repeats so far, by listing the repeat as a string,
however, this means that I will need to copy and paste the whole genome of the species of interest into a string
every time that I run the program, which is cumbersome and inefficient.  

What I need to figure out next:
1)	How to import FASTA files into an iPython Notebook
2)	A way to identify repeat sequences as a string, within a larger data set that is not a string in FASTA format.
3)	Remove white space from FASTA files – this is because some spacers will cross the end of a line, and beginning of the next, and still need to be identified.
4)	A way to list spacer sequences individually for a particular CRISPR system – i.e. with line breaks.

Possible solutions:
1)	set genome as variable, then make it a string, this is dependent on importing file.


