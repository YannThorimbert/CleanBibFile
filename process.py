"""(c) Yann Thorimbert
Python script removing field from latex bibliography files using user defined
patterns. Also add cosmetic blank lines between bib entries.
"""
from __future__ import print_function


fn_source = "biblio.bib" #the name of the bib file to process
fn_target = "cleanedBiblio.bib" #the name of the bib file to produce
fields_to_remove = ["file", "abstract"] #non case sensitive
integrity_check = ["author", "title"] #fields that must contain each entry
add_blank_line = True #add blank line between unspaced bibliogrphy entries
auto_pattern = True #False : remove only the exact patterns in fields_to_remove


if auto_pattern:
    patterns = []
    for equal in [" =", "="]:
        for field in fields_to_remove:
            patterns.append(field+equal)
else:
    patterns = fields_to_remove


f = open(fn_source, "r")
lines = f.readlines()
f.close()


entries = set()
removing = False
ending = ""
count = 0
f = open(fn_target,"w")
for i,line in enumerate(lines):
    low = line.lower().replace("\n","")
    for pattern in patterns:
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



#verify integrity
f = open(fn_target, "r")
lines = f.readlines()
f.close()

content = {}
current = None
for line in lines:
    while "\t" in line:
        line = line.replace("\t","    ")
    if "@" in line:
        current = line.split("{")[1].split(",")[0]
        if not current:
            raise Exception("Invalid entry")
        content[current] = {}
    if "=" in line:
        field = line.split("=")[0].replace(" ","").lower()
        content[current][field] = line.split("=")[1].replace("\n","")

count = 0
for article in content:
    for field in integrity_check:
        if not field in content[article]:
            print("No", field, "in", article, "!!!")
            count += 1

print(count,"integrity warnings found in the produced file.")




