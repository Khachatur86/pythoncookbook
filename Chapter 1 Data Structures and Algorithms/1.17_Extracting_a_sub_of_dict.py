from pprint import pprint
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}


p1 = {k:v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

p2 = {k:v for k, v in prices.items() if k in tech_names}

pprint(p1)
pprint(p2)

p1 = dict((k, v) for k, v in prices.items() if v > 200)

p2 = {k: prices[k] for k in prices.keys() & tech_names}

pprint(p1)
pprint(p2)