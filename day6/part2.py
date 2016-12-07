from collections import Counter
from operator import itemgetter

i = 0
message = [[] for _ in range(8)]
message_final = ''

with open('input') as f: 
    for line in f:
        line = line.strip()
        for i in range(8):
            message[i].append(line[i])

for x in range(len(message)):
    c = Counter(message[x]).most_common()
    print(c)
    c.sort(key=itemgetter(1))
    message_final = message_final + c[0][0]

print(message_final)
