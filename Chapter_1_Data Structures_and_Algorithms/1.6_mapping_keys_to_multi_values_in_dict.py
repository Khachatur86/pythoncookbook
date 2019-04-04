from collections import defaultdict

d = defaultdict(list)
print(d)
d['a'].append(4)
d['a'].append(7)
print(d)

# Или же можно
d = defaultdict(set)
d['a'].add(22)
d['a'].add(21)
d['a'].add(245)
print(d)