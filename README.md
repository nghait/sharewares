# sharewares/convertgbk.py   
Bioinformatics makes life easier especially for biological beginner, it was just a scorching search online and I found how to convert multiple gbk to single one.
It's got made a little nicer to run, this program is a ray in the hope that it can help someone save time or just simply enjoy the code.

---About me---convertgbk.py Version 1.1 designed by Nguyen Hai Tuan at National Institute of Hygiene and Epidemiology, Hanoi, Vietnam.
You are free to use and redistribute this program, the author has neither responsibility for your well-being nor the accuracy of your data.
The converter convertgbk.py program was designed to convert multiple genbank file to single genbank file.
This is designed for use in Linux and not tested in other operating systems, and the current document is not a comprehensive explanation how to use provided code.
It is assumed that users already known the basic of bash/shell and Python or Biopython programming.

*** When to use this program: when you need to convert a multiple genbank file to single gbk file format. One can distinguish this function from cat function which concatenates files into single file with multiple records.  

Installation:

Super easy as download-and-run it in the current working directory, or make PATH environment variable to the program.

Dependencies:

There are dependencies as required to run Python 3, Piopython 1.6 on Linux like system (Ubuntu 14 or higher, no hint for earlier born)

Type for help:
$ python convertgbk.py -h

Syntax to convert multiple gbk file to single gbk file:
$ python convertgbk.py -i \<inputfile> -o \<outputfile>

or of cause use canonical chmod +x to make it executable.

$ ./convertgbk.py -i \<inputfile> -o \<outputfile>

example of use:

$ ./convertgbk.py -i mygenome.gbk -o MerGed

Where mygenome.gbk is the multiple gbk file to convert and MerGed is the core name given to output file (MerGed.gbk for instance).
It is resulting MerGed.gbk, which is the single gbk file.

Finally, to run in batch mode or in pipe, it's your pool to swim. 
Good Luck!
