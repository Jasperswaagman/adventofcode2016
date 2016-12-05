import re

with open("smallinput", "r") as fp:
    for line in fp:
        line = line.strip()
        
        # Store the checksum so we can compare it
        checksum = re.search("\[(\w{5})\]", line)
        checksum = checksum.group(1)

        # Strip the checksum and sector ID
        r = re.search("([a-z-]+)(\d+)", line)
        enc_name = r.group(1).replace("-","")
        sector_id = r.group(2)
            
