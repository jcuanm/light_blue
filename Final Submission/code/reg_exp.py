""";; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer."""
import re, mmap

# opens the file to read 
def reg_exp(pgn):
  with open(pgn, 'r+') as f:
    data = mmap.mmap(f.fileno(), 0)

    # searches for the specified string combination 
    reg1 = re.search('WhiteElo (.*)', data)

    # grabs the string right after the flag and stores it in a variable
    final_string1 = reg1.group(1)
    reg2 = re.search('BlackElo (.*)', data)
    final_string2 = reg2.group(1)
    reg3 = re.search('Result (.*)', data)
    final_string3 = reg3.group(1)
    
    WhiteElo = int(final_string1[1:-3])
    BlackElo = int(final_string2[1:-3])
    if int(final_string3[1]) == 0:
      # black wins
      return (WhiteElo, BlackElo, "black")
    if int(final_string3[3]) == 2:
      # tie
      return (WhiteElo, BlackElo, "tie")
    else:
      # white wins
      return (WhiteElo, BlackElo, "white")
      
  f.close()


