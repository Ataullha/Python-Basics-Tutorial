"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
"""
import math
import re

m = {}

with open('poem.txt', 'r') as f:
    poem = f.read()

max_occ = -1 * math.inf
words = poem.split(" ")

for word in words:
    if word not in m:
        word = word.replace('\n', '')
        m[word] = 1
    else:
        m[word] = m[word] + 1

print(m)

# print(max_occ)
for word in m.keys():
    max_occ = max(max_occ, m[word])

print(max_occ)

for key, value in m.items():
    if value == max_occ:
        print(key)

"""
stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
pe ratio = price / earnings per share
price to book ratio = price / book value
Your input format (stocks.csv) is,

Company Name	Price	Earnings Per Share	Book Value
Reliance	1467	66	653
Tata Steel	391	89	572
Output.csv should look like this,

Company Name	PE Ratio	PB Ratio
Reliance	22.23	2.25
Tata Steel	4.39	0.68
"""

with open('stocks.csv', 'r') as f:
    s = f.read()
print(s)

ls = re.split('\n', s)
ls.remove('Company Name,Price,Earnings Per Share, Book Value')
lines = []
for line in ls:
    words = line.split(',')
    pe_ratio = int(words[1]) / int(words[2])
    pb_ratio = int(words[1]) / int(words[3])
    lines.append(words[0] + ',' + str(pe_ratio) + ',' + str(pb_ratio))

print(lines)
with open('output.csv', 'a') as f:
    f.write('Company Name,Price,Earnings Per Share, Book Value' + '\n')
    for line in lines:
        f.write(line + '\n')
