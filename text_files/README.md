
README

This program is for finding spacers between CRISPR repeats in bacterial/archaeal genomes

it takes two arguments.  The first argument is the fasta file which contains the genome, 
to be scanned through

the second argument is the CRISPR to find the spacer of.  CRISPRS for the corresponding 
example genomes are found in the Example CRISPRs file, in the data folder.  They should
be copied to the clipboard, so that they can be pasted quickly into a terminal window
as a second argument.

the final piece of the code, which is to print a graph of the beginning and end locations
of the spacer along the genome, is not working.  Isaac showed me a way to create a 
dataframe from variables stored in my code, however that cell was accidentially deleted
before a git commit happened, so it was lost.  Strangely, my .ipynb of this project still 
creates the graphs, even though the dataframe that is dependant on is no longer there.

The Shell script to be run in command line is Nico_script.  the python notebook, which 
creates the appropriate bar graph, is 1st_spacer.ipynb.  An example of what that graph 
looks like is available in the results folder.