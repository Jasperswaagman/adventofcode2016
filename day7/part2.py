import re

i = 0

def has_hypernet_ABBA(hypernet_sequences):
    for l in hypernet_sequences:
        print(l)
        if ABBA_detector(l): print(l); return True

def ABBA_detector(pattern):
    for i in range(1, len(pattern) - 2): 
        if pattern[i] == pattern[i+1] and pattern[i-1] == pattern[i+2] and pattern[i] != pattern[i+2]: 
            return True


with open('input') as f: 
    for line in f:
        line = line.strip()
        hypernet_sequences = re.findall('(\[.*?\])', line) # Need to get all the bracket groups and join them, then the rest
        print(hypernet_sequences)
        if not has_hypernet_ABBA(hypernet_sequences):
            ip_address = re.findall('(.*?)(?:\[.*?\]|$)', line) # Get the rest of the IP address
            ip_address = list(filter(len, ip_address))
            for x in ip_address:
                if ABBA_detector(x): i += 1; print(i); break
        
print('{0} IPs that support TLS'.format(i))
        
