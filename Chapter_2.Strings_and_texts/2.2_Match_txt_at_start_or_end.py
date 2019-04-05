filename = 'spam.txt'
print(filename.startswith('fil'))
print(filename.endswith('txt'))

import os

print(os.listdir('.'))
filenames = os.listdir('.')
names = [name for name in filenames if name.endswith(('.py', 'che'))]
print(names)

print(any(name.endswith('.py') for name in filenames))