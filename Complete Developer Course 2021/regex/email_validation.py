import re

pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# with open('email.list', mode='r') as elist:
#   while email := elist.readline():
#     email.strip('\n')
#     print(email, end=': ')
#     if pattern.fullmatch(email):
#       print('yes')
#     else:
#       print('no')

with open('email.list', mode='r') as elist:
  emails = elist.read()
  print(emails)
  matches = pattern.search('kritagya.0398@gmail.com 17145@iiitu.ac.in kritagya.khandelwal@314ecorp.com')
  print(matches)
