import re
from collections import Counter
from operator import itemgetter

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decoder(char, shift):
    # Make a loop trough the alphabet
    return alphabet[(alphabet.index(char) + shift) % 26]


with open('input', 'r') as fp:
    for line in fp:
        line = line.strip()
        
        # get the needed info
        r = re.search('([a-z-]+)(\d+)\[(\w{5})\]', line)
        enc_name = r.group(1).replace('-','')
        sector_id = int(r.group(2))
        checksum = r.group(3)

        letters = []
        for c in enc_name: letters.append(c)
        letters = sorted(letters)
        letters = Counter(letters).most_common()
        letters.sort(key=itemgetter(0))
        letters.sort(key=itemgetter(1), reverse=True)
        most_common = [] 
        for c in range(5): most_common.append(letters[c][0])
        # If room is valid 
        if ''.join(most_common) == checksum: 
            decoced_line = ''
            for c in enc_name: decoced_line = decoced_line + decoder(c, sector_id)
            if 'northpole' in decoced_line: print(sector_id); break

