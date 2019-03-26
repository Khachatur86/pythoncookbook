record = '....................100 .......513.25 ..........'
# cost = int(record[20:23]) * float(record[31:38])


SHARES = slice(20, 23)
PRICE = slice(31,38)
cost  = int(record[SHARES]) * float(record[PRICE])
print(cost)
a = slice(3, 50, 1)
s = 'HELLOWORLD'
print(a.indices(len(s)))

def gcd(a, b):
  while b != 0:
    rem = a % b
    a = b
    b = rem
  return a

print(gcd(78, 3003))