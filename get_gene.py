#!/usr/bin/env python
f=open("VSPII_NAGP1.faa","r");
opened = False
for line in f :
    if(line[0] == ">") :
        if(opened) :
            of.close()
        opened = True
        of=open("%s.fa" % (line[1:].rstrip()), "w")
        print(line[1:].rstrip())
    of.write(line)
of.close()
