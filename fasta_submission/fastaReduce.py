#!/usr/bin/env python

import sys
import re
import os
import os.path
import shutil
from optparse import OptionParser
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein

usage= """
Takes the full fasta file of a database used to search for PSMs and returns only sequences with identified peptide matches

usage: %prog [-d FILE] [-p FILE] [-o STR]"""

parser = OptionParser(usage=usage, version="%prog 0.1")

parser.add_option("-d", "--database", dest="dbFile",
                  help="Specify the fasta database file used for searching PSMs",
                  metavar="FILE")
parser.add_option("-p", "--proteinIDs", dest="protFile",
                  help="Specify a txt file with all the proteins identified from the fasta file in a list without a header",
                  metavar="FILE")
parser.add_option("-o", "--output_name", dest="outputFile",
                  help="Specify the your desire output file name",
                  metavar="STR")

(options, args) = parser.parse_args()

#Makes sure all mandatory options appear
mandatories = ["dbFile", "protFile"]
for m in mandatories:
	if not options.__dict__[m]:
		print("A mandatory option is missing!\n See the HELP menu - 'fastaReduce.py -h'" )
		parser.print_help()
		exit(-1)
#Sets the default outputfile name	
if options.outputFile == None:
	outputName = options.dbFile
	outputFileName = outputName + "_only_PSM_match_sequences.fasta"
else: 
	outputName = options.outputFile
	outputFileName = outputName + ".fasta"

#Set variables based on collected input
outputFile = open(outputFileName, "w")

#recordIx = SeqIO.index(options.dbFile, "fasta")
cleanDict = {}
record_ids = list()
for record in SeqIO.parse(options.dbFile, "fasta"):
	if record.id not in record_ids:
		record_ids.append(record.id)
		cleanDict[record.id] = record


resultsDict = {}

protFileRead = open(options.protFile, "r").readlines()

for element in protFileRead:
	element = element.strip("\n")
	try:
		seq_record = cleanDict[element]
		str_seq = str(seq_record.seq)
		str_seq = re.sub('[Xx\*]',"", str_seq)
		seq_record.seq = Seq(str_seq, generic_protein)
		resultsDict[element] = seq_record
	except:
		print("WARNING: A sequence for the following does not exist in this fasta file: " + str(element))

SeqIO.write(resultsDict.values(), outputFile, "fasta")
