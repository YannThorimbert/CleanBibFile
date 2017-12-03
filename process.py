"""(c) Yann Thorimbert
Python script removing field from latex bibliography files using user defined
patterns. Also add cosmetic blank lines between bib entries.
"""
from __future__ import print_function


fn_source = "test.bib" #the name of the bib file to process
fn_target = "cleanedBiblio.bib" #the name of the bib file to produce
fields_to_remove = ["file =", "abstract =", "file =", "abstract="] #non case sensitive
add_blank_line = True #add blank line between unspaced bibliogrphy entries

f = open(fn_source, "r")
lines = f.readlines()
f.close()


removing = False
ending = ""
count = 0
f = open(fn_target,"w")
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
    else:
        if ",\n" in line or "}\n" in line:
            if "}\n" in line:
                print(line)
                assert "}\n" == line
                f.write("}\n")
            removing = False
f.close()

print("Finished to process",fn_source,"to",fn_target,"\nRemoved",count,"lines.")






