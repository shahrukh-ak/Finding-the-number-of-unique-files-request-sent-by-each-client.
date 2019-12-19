#!/usr/bin/python
import sys
(last_key, value) = (None, None)
i = 0

for line in sys.stdin:
    (key, new_value) = line.split('\t')

    if last_key and key != last_key:
        
               
        print('\n Client: %s  has %s different file requests.' % (last_key, i))
        (last_key, value) = (key, new_value)
        i=1

    else:
        if value != new_value:
            i=i+1    
        (last_key, value) = (key, new_value)

if last_key:
    
    print('\n Client: %s  has %s different file requests.\n' % (last_key, i))


  
       
