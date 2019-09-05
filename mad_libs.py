#! /usr/bin/env python3
# mad_libs.py - read in a file with text like
'''
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
'''
# then prompt the user to replace each ADJECTIVE|NOUN|VERB with his/her
# own word, print the finished text to screen as well as copy to the
# user's clipboard.
# If the file is not found, ask the user if he/she'd like to do the
# panda text, otherwise quit.

import sys, os, re, pyperclip

DEFAULT_TEXT = 'The ADJECTIVE panda walked to the NOUN and then VERB (past tense). A nearby NOUN was unaffected by these events.'
source_text = DEFAULT_TEXT
result_text = ''
ro = re.compile(r'(ADJECTIVE|NOUN|VERB \(past tense\))')
vowel_ro = re.compile(r'[aeiouAEIOU]')

def start_game():
  global source_text 
  print('******** MAD LIBS ********\n')
  if len(sys.argv) < 2 or os.path.exists(sys.argv[1]) is not True:
    use_default_text = input('No input file found. Use default text? y/n\t')
    if use_default_text.lower() != 'y' and use_default_text != '':
      print('Bring your text next time. Bye!')
      sys.exit()
    else:
      play_game()
  else:
    source_file = open(sys.argv[1])
    source_text = source_file.read()
    source_file.close()
    play_game()    

def play_game():
  global result_text
  last_end = 0
  while True:
    mo = ro.search(source_text, pos=last_end)
    if mo is None:
      result_text += source_text[last_end:]
      end_game()
      break
    found_start = mo.start()
    found_end = mo.end()
    matched_text = mo.group()
    sub_text = input('Enter a' + ('n ' if vowel_ro.search(matched_text[0]) is not None else ' ') + matched_text.lower() + ':\t')
    result_text += source_text[last_end:found_start] + sub_text
    last_end = found_end


def end_game():
  print("**** We're Done! ****")
  print('\n' + result_text + '\n')
  pyperclip.copy(result_text)
  print('**** The text is also in your clipboard! Have fun! ****')

start_game()