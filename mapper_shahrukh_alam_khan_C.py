#!/usr/bin/python
import sys

for lines in sys.stdin:
    lines = lines.strip().split(' ')
    print("%s\t%s"%(lines[0], lines[3]))


