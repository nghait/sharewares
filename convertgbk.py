#!/usr/bin/python
# $ which python # to your favorite

import sys, getopt
if len(sys.argv) > 5 \
   or len(sys.argv) == (4 or 3):
   print 'Syntax error, please check your parameters'
   # print len(sys.argv)
   sys.exit(1)

if len(sys.argv) == 1:
   print '---About me---convertgbk.py Version 1.1 designed by inspiration of code and meaning.'
   print 'You are free to use, modify and redistribute this program, the author has neither responsibility for your well-being nor the accuracy of your data.'
   print 'The converter convertgbk.py program was designed to convert multiple genbank file to single genbank file.'
   print 'Type \"python convertgbk.py -h\" for help on the converter.'
   # print len(sys.argv)
   sys.exit(1)
def main(argv):
   inputfile = ''
   outputfile = ''
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["infile=","outfile="])
   except getopt.GetoptError:
      print 'convertgbk.py -i <inputfile> -o <outputfile>'
      print 'You need to provide input and output names! Please check -i and -o parameters'
      sys.exit(2)
   
   for opt, arg in opts:
      if opt == '-h':
         print '---Help---'
         print 'convertgbk.py -i <inputfile> -o <outputfile>'
	 print 'Inputfile is a multiple gbk file, outputfile is the name of single gbk file.'
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
   for rec in SeqIO.parse(open(infile,"rU"), "genbank"):
         gbkrec += rec
         gbkrec.id = "genome"
         gbkrec.description = "combination of gbk sequences"
         SeqIO.write(gbkrec, namefile + '.gbk', "genbank")
         
   Nfile=str(namefile+'.gbk')
   import os.path
   if os.path.isfile(Nfile) and os.access(Nfile, os.R_OK):
         print 'Output file', namefile + '.gbk', 'has been successfully generated!'
         print '----------------------------------------------'
         print 'Thank you for using single genbank file converter'   
   else:
         print 'Sorry ! File type is not suitable to be converted !!!' 
         print 'You need to provide a multiple genbank file as input, please check your input file.'
         sys.exit(2)
if __name__ == "__main__":
   main(sys.argv[1:])
