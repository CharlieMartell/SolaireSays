#!/usr/bin/env python
import textwrap, random
from utils.quote import QUOTES, NPCS, NPC_ASCII

def get_border(lines, index):
    """
    Creates a border around a given npc quote
    """
    if len(lines) < 2:
        return [ "<", ">" ]
    elif index == 0:
        return [ "/", "\\" ]
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    else:
        return [ "|", "|" ]

def normalize(str, length):
    """
    Normalizes text to fit in bubble nicely.
    """
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def bubble(str, length=40):
    """
    Bubbles text
    """
    bubble = []
    lines = normalize(str, length)
    bordersize = len(lines[0])
    bubble.append("  " + "_" * bordersize)
    for index, line in enumerate(lines):
        border = get_border(lines, index)
        bubble.append("%s %s %s" % (border[0], line, border[1]))
    bubble.append("  " + "-" * bordersize)
    return "\n".join(bubble)

def random_npc_quote():
    """
    Gets a random npc and quote and returns tuple of them.
    """
    npc = random.choice(NPCS)
    quote = random.choice(QUOTES[npc])
    full_quote = "{} - {}".format(quote, npc)
    return (npc, full_quote)

def solaire_says(npc, quote, length=40):
    return bubble(quote, length) + NPC_ASCII[npc]

def main():
    (npc, quote) = random_npc_quote()
    print solaire_says(npc, quote)

if __name__ == '__main__':
    main()
