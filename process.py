"""(c) Yann Thorimbert
Python script removing field from latex bibliography files using user defined
patterns. Also add cosmetic blank lines between bib entries.
"""
from __future__ import print_function


fn = "biblio.bib" #the name of the bib file to process
fields_to_remove = ["file =", "abstract =", "file =", "abstrac ="] #non case sensitive
add_blank_line = True #add blank line between unspaced bibliogrphy entries

f = open(fn, "r")
lines = f.readlines()
f.close()


removing = False
count = 0
f = open(fn+"lol","w")
for i,line in enumerate(lines):
    low = line.lower().replace("\n","")
    for pattern in fields_to_remove:
        if pattern in low:
            print("--> Removing field from", line)
            removing = True
            count += 1
            break
    if not removing:
        if add_blank_line:
            if "@" in line and lines[i-1]:
                print("--> Added blank line before", line)
                f.write("\n")
        f.write(line)
    if "}," in line:
        removing = False
f.close()

print("Finished to process",fn,"\nRemoved",count,"lines.")






