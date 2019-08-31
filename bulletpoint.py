#! /usr/bin/env python3
# bulletpoint.py - A program to add * in front of each line of your
# copied list lines

import pyperclip
print('>>>> Processing the lines in clipboard...')
# get the lines copied in the clipboard currently
# split by newline to put each line into an array
lines = pyperclip.paste().split('\n')

# add "*" and a space in front of each line in the lines array
# join them with newline into one string
# copy that string to clipboard
pyperclip.copy('\n'.join(['* ' + line for line in lines]))

# tell the user that the job is done
print('>>>> Bullet points added. Paste at will.\nHave a good day!')

