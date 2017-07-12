#!/usr/bin/python

import sys, getopt
if len(sys.argv) > 5 \
   or len(sys.argv) == (4 or 3):
   print 'Syntax error, please check your parameters'
   # print len(sys.argv)
   sys.exit(1)

if len(sys.argv) == 1:
   print '---About me---convertfasta.py Version 1.1 designed by inspiration of code and meaning.'
   print 'You are free to use, modify and redistribute this program, the author has neither responsibility for your well-being nor the accuracy of your data.'
   print 'The converter convertfasta.py program was designed to convert multiple fasta file to single fasta file.'
   print 'Type \"python convertfasta.py -h\" for help on the converter.'
   # print len(sys.argv)
   sys.exit(1)
def main(argv):
   inputfile = ''
   outputfile = ''
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["infile=","outfile="])
   except getopt.GetoptError:
      print 'convertfasta.py -i <inputfile> -o <outputfile>'
      print 'You need to provide input and output names! Please check -i and -o parameters'
      sys.exit(2)
   
   for opt, arg in opts:
      if opt == '-h':
         print '---Help---'
         print 'convertfasta.py -i <inputfile> -o <outputfile>'
	 print 'Inputfile is a multiple fasta file, outputfile is the name of single fasta file.'
         sys.exit(0)
      elif opt in ("-i", "--infile"):
         inputfile = arg
      elif opt in ("-o", "--outfile"):
         outputfile = arg

   print 'Your input file is', inputfile, 'with user-supplied arguments', sys.argv[1:]
   print '----------------------------------------------'
   from Bio import SeqIO
   gbkrec =''
   infile = inputfile
   namefile = str(outputfile)
   for rec in SeqIO.parse(open(infile,"rU"), "fasta"):
         gbkrec += rec
         gbkrec.id = "draftgenome"
         gbkrec.description = "combination of fasta contigs sequences"
         SeqIO.write(gbkrec, namefile + '.fa', "fasta")
   Nfile=str(namefile+'.fa')
   import os.path
   if os.path.isfile(Nfile) and os.access(Nfile, os.R_OK):
         print 'Output file', namefile + '.fa', 'has been successfully generated!'
         print '----------------------------------------------'
         print 'Thank you for using single fasta file converter'   
   else:
         print 'Sorry ! File type is not suitable to be converted !!!' 
         print 'You need to provide a multiple fasta file as input, please check your input file.'
         sys.exit(2)
if __name__ == "__main__":
   main(sys.argv[1:])
