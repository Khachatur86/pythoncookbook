text = 'yeah, but no, but yeah, but no, but yeah'

print("text.startswith('yeah') - ", 
                               text.startswith('yeah'))
print("text.endswith('no') - ",
                         text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

# print(text[10:])

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
  print('yes')
else:
  print('no')


if re.match(r'\d+/\d+/\d+', text2):
  print('yes')
else:
  print('no')


datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
  print('yes')
else:
  print('no')

# match() always tries to find the match at the start of a string.
if datepat.match(text2):
  print('yes')
else:
  print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

print(datepat.findall(text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

m = datepat.match('11/27/2012')

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
# print(m.group(4))

print(m.groups())
month, day, year = m.groups()
print(month, day, year)

for month, date, day in datepat.findall(text):
  print(f'{month} - {date} - {day}')