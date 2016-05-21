''' splits PGN files with multiple games into 
	multiple PGN files with a game each '''

import sys,os
import re

''' WesleySo was the last file split '''
small_pgn=open("WesleySo.pgn") #read original alignment file  
pgn_content=small_pgn.read() 
myre = re.compile("\r\n\r\n\r\n")
pgn_list = myre.split(pgn_content)

# i variable changed manually for each split
i = 15791
for small_file in pgn_list:
        name = str(i) + ".pgn"
        f = open(name, 'w')
        f.write(small_file)
        f.close()
        i += 1

