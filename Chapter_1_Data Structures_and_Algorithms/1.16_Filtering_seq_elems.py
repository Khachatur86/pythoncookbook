my_list = [1, 4, -5, 10, -7, 2, 3, -1]
pos_num_list = [n for n in my_list if n > 0]
print(pos_num_list)

neg_num_list = [n for n in my_list if n < 0]
print(neg_num_list)

# or same by with using genexpressions

pos_n = (n for n in my_list if n > 0)
neg_n = (n for n in my_list if n < 0)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
  try:
    x = int(val)
    return True
  except ValueError:
    return False


ivals = list(filter(is_int, values))

print(ivals)

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n>5 for n in counts]
from itertools import compress

print(list(compress(addresses, more5)))