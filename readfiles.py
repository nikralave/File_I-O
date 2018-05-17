# f  = open('data.txt', 'r')
# lines = f.readlines()
# f.close()
# print(lines)


# f  = open('data.txt', 'r')
# lines = f.read().split('\n')
# f.close()
# print(type(lines))

import re
import collections

text = open('1155-0.txt').read().lower()
words = re.findall('\w+', text)

long_words = []

for word in words:
    if len(word)>=5:
        long_words.append(word)

most_common = collections.Counter(long_words).most_common(10)

print(most_common)