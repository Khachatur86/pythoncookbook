from fnmatch import fnmatch, fnmatchcase

# fnmatch - не учитывает регистр 
# fnmatchcase - учитывает регистр

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

names_bool = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(names_bool)

print("fnmatchcase('foo.txt', '*.TXT') - ",fnmatchcase('foo.txt', '*.TXT'))

addresses = [
  '5412 N CLARK ST',
  '1060 W ADDISON ST',
  '1039 W GRANVILLE AVE',
  '2122 N CLARK ST',
  '4802 N BROADWAY',
]

addrs_bool1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]

print(addrs_bool1)

addrs_bool2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

print(addrs_bool2)

