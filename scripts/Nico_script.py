import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import numpy

input_file = sys.argv[1]
first_repeat = sys.argv[2]


def main():

	#import the data, in a way that allows the REs to work.
	wgs = open(input_file, 'r').read()
	print (len(wgs))
	
	#munging data cell
	wgs = wgs.replace('\n', '')
	wgs = str(wgs)
	
	#starting location of 1st CRISPR repeat
	first_loc_start = []
	p = re.compile(first_repeat)
	for m in p.finditer(wgs):
		first_loc_start.append(m.start())
	#this is the first starting position
	first_it_start_1 = (first_loc_start[0])
	#this is the second starting position
	second_it_start_1 = (first_loc_start[1])
	#here is a test to make sure that the input is a string.  Repeats is a string, so it passes
	
	#this cell creates variables first_it_end_1,second_it_end_1 which are the end locations of the 1st 
	#and 2nd interations of the CRISPR repeat
	first_loc_end = []
	p = re.compile(first_repeat)
	for m in p.finditer(wgs):
		first_loc_end.append(m.end())
		d1 = m.end()
	#this is the first ending position
	first_it_end_1 = (first_loc_end[0])
	#this is the second ending position
	second_it_end_1 = (first_loc_end[1])
	
	#this shows me the starting and end points of the repeat, 
	#and also shows the sequence, to prove that it is a repeat.
	p = re.compile(first_repeat)
	for m in p.finditer(wgs):
		print (m.start(), m.group(), m.end())
		
		#this shows me:
	#the start position, and end position of that spacer, 
	#the sequence of the spacer,
	#proving that it is the spacer between two CRISPRS.	
	#the length of the spacer

	spacer = (wgs[first_it_end_1:second_it_start_1])
	print (first_it_end_1,second_it_start_1)
	print (spacer)
	print (len(spacer))
	
	
	output_table.plot(kind='bar')
	plt.ylabel('Genomic Location (nucleotide)')
	plt.xlabel('end of 1st repeat, beginning of 2nd repeat')
	plt.title('Location of Spacer in genome')

	axes = plt.gca()
	axes.set_ylim([0,len(wgs)])
	plt.savefig(output_table.pdf)
	
	
	#this is a test to make sure that wgs is a string, so that regex work on it
def test(wgs):
    for r in wgs:
        assert type(r) is str, 'Spacers need to be strings in order for regular expressions to work'
        return()
	
main()