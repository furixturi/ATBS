#! /usr/bin/env python3
# pw.py - An insecure password locker program

import sys, pyperclip

PASSWORDS = {
  'email': 'ASDFWQETSFDHsfgsldkhfa',
  'blog': 'qwe8d67f34sfg',
  'bank': '1234apsdo8fy245_'
}

if len(sys.argv) < 2:
  print('Usage: python3 pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for "{}" copied into clipboard.\nPaste as you will.'.format(account))
else:
  print('There is no account named "{}"'.format(account))