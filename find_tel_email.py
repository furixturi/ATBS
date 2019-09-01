#! /usr/bin/env python3
# find_tel_email.py - find US tel numbers and emails from copied text
import re, pyperclip

phoneRegex = re.compile(r'''(       # group 0 the whole number
  \(?                                   # opening parenthesis
  (\d{3})?                          # group 1 area code
  \)?                                   # closing parenthesis
  [\s\-.]?                              # separator
  (\d{3})                           # group 2 first 3 digits
  [\s\-.]?                              # separator
  (\d{4})                           # group 3 last 4 digits
  (\s*                              # group 4 whole extension
  [ext|x|ext.]                          # extension text prefix
  \s*                                   # maybe some spaces
  (\d{2,5}))?                       # group 5 extension digits
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+               # username
  @                               # @ symbol
  [a-zA-Z0-9.-]+                  # domain name
  \.[a-zA-Z]{2,4}                 # dot something
)''', re.VERBOSE)

def find_phone_numbers(text):  
  phone_numbers_raw = phoneRegex.findall(text)
  # [('415-555-9999', '415', '-', '555', '-', '9999', '', '', ''), ('212-555-0000x04', '212', '-', '555', '-', '0000', 'x04', 'x', '04')]
  phone_numbers_formatted = []
  for groups in phone_numbers_raw:
    phone_number = '-'.join([groups[1], groups[2], groups[3]])
    if groups[5] != '':
      phone_number += 'x' + groups[5]
    phone_numbers_formatted.append(phone_number)
  return phone_numbers_formatted

def find_emails(text):
  emails = emailRegex.findall(text)
  return emails

print('Searching for telephone numbers and email addresses in clipboard...\n')

text = pyperclip.paste()
result_text = '>>> Found the following phone numbers:\n    ' + '\n    '.join(find_phone_numbers(text))
result_text += '\n\n>>> Found the following email addresses:\n    ' + '\n    '.join(find_emails(text))

pyperclip.copy(result_text)
print(result_text)
print('\nThe above information is copied to clipboard and ready to paste.')
