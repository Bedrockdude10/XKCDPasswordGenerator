#!/usr/bin/env python3
import argparse
import random
import string

parser = argparse.ArgumentParser()

parser.add_argument("-w", "--words", default=4, action="store", type=int, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", default=0, action="store", type=int, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", default=0, action="store", type=int, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", default=0, action="store", type=int, help="insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()

f = open("words.txt", "r")

wordList = f.readlines()

characters = []

for string in wordList:
        nstring = string.strip()
        nstring = nstring.replace("-","")
        nstring = nstring.replace("'","")
        nstring = nstring.lower()
        characters.append(nstring)
        
f.close()

password = []

if args.words:
        nWords = args.words
else:
        nWords = 4

if args.caps:
        nCaps = args.caps
else:
        nCaps = 0

if args.numbers:
        nNumbers = args.numbers
else:
        nNumbers = 0

if args.symbols:
        nSymbols = args.symbols
else:
        nSymbols = 0

def addWords():
        ## picking random words from the list
        for i in range(nWords):
                password.append(random.choice(characters))
        return password

def addCaps():
        ## picking random words and capitalizing them
        for i in range(nCaps):
                x = random.choice(range(0, nWords))
                password[x] = password[x].capitalize()
        return password

def addNumbers():
        ## inserts random numbers
        for i in range(nNumbers):
                x = random.choice(range(0, nWords))
                l = random.choice(range(0, len(password[x])))
                string = password [x]
                substring1 = string[:l]
                substring2 = string[l:]
                password[x] = substring1 + str(l) + substring2
        return password

## picking random words and capitalizing them
for i in range(nSymbols):
        random.choice(password).capitalize()

addWords()
addCaps()
addNumbers()
print("".join(password))
