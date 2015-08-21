#!/usr/bin/env python
import textwrap, random
from quote import QUOTES, NPCS

def build_solaire():
   return """
     __    ___________    __
     \ \  | ___| |___ |  / /
      \ \ ||___| |___|| / /
       \ \|    | |    |/ /
        \_|____|_|____|_/
    """

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]
    elif index == 0:
        return [ "/", "\\" ]
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    else:
        return [ "|", "|" ]

def normalize(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]  

def bubble(str, length=40):
    bubble = []

    lines = normalize(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def solaire_says(str, length=40):
    return bubble(str, length) + build_solaire()

def random_quote():
    npc = NPCS[0] # To be randomized when more npcs are supported 
    quote = random.choice(QUOTES[npc])
    full_quote = "{} - {}".format(quote, npc)
    return full_quote
    
def main():
    quote = random_quote()
    print solaire_says(quote)

if __name__ == '__main__':
    main()
