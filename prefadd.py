import sys
import re

#############################################
### Currently works for Turtle files only ###
### Give it a file and your wanted prefix ###
### And the program adds it into the file ###
### So you can reference it (for GraphDB) ###
### The file MUST be in the same folder!! ###
#############################################

### Command line args ###
filepath = sys.argv[1]
desiredprefix = sys.argv[2]

### Parsing file for base prefix ###
file = open(filepath, 'r')
lines = file.readlines()
baseprefixpattern = re.compile('@prefix *: *<.+> *.')

for i, line in enumerate(lines):
    for match in re.finditer(baseprefixpattern, line):
        unformattedline = line.strip()
        linenumber = i
        break
    break

file.close()

### String manipulation ###
splitpattern = re.compile(' +:')
prefixline = re.split(splitpattern, line)
desiredprefixline = prefixline[0] + ' ' + desiredprefix + ': ' + prefixline[1].strip() + '\n'

lines[linenumber] = unformattedline + '\n' + desiredprefixline 

### Write back to file ###
with open(filepath, 'w') as writer:
    writer.writelines(lines)

print('Added desired prefix: ' + desiredprefixline)
