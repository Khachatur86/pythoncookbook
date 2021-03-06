from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['not'])

morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
  word_counts[word] += 1

print(word_counts['eyes'])
word_counts.update(morewords)

print(word_counts.most_common(3))

a = Counter(words)
b = Counter(morewords)

print('a=', a)
print('b=', b)
c = a + b
print('c=', c)
d = a - b
print('d=', d)