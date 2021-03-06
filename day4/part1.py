import re
from collections import Counter
from operator import itemgetter

sum_sector_ids = 0

with open("input", "r") as fp:
    for line in fp:
        line = line.strip()
        
        # get the needed info
        checksum = re.search("\[(\w{5})\]", line)
        checksum = checksum.group(1)
        r = re.search("([a-z-]+)(\d+)", line)
        enc_name = r.group(1).replace("-","")
        sector_id = int(r.group(2))

        letters = []
        for c in enc_name: letters.append(c)
        letters = sorted(letters)
        letters = Counter(letters).most_common()
        letters.sort(key=itemgetter(0))
        letters.sort(key=itemgetter(1), reverse=True)
        most_common = [] 
        for c in range(5): most_common.append(letters[c][0])
        if "".join(most_common) == checksum: sum_sector_ids += sector_id

    print(sum_sector_ids)
