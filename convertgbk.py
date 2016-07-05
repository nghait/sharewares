#!/usr/bin/python
# $ which python # to your favorite

import sys, getopt
if len(sys.argv) > 5 \
   or len(sys.argv) == (4 or 3):
   print 'Syxtax error, please check your parameters'
   # print len(sys.argv)
   sys.exit(1)

if len(sys.argv) == 1:
   print '---About me---convertgbk.py Version 1.1 designed by Nguyen Hai Tuan at National Institute of Hygiene and Epidemiology, Hanoi, Vietnam'
   print 'You are free to use and redistribute this program, the author has neither responsibility for your well-being nor the accuracy of your data.'
   print 'The converter convertgbk.py program was designed to convert multiple genbank file to signle genbank file.'
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
   for rec in SeqIO.parse(open(infile,"r"), "genbank"):
         gbkrec += rec
         gbkrec.id = "mergedseq"
         gbkrec.description = "merged seq"
         SeqIO.write(gbkrec, namefile + '.gbk', "genbank")
         
   print 'Output file', namefile + '.gbk', 'has been successfully generated!'
   print '----------------------------------------------'
   print 'Thank you for using single genbank file converter'   

if __name__ == "__main__":
   main(sys.argv[1:])
