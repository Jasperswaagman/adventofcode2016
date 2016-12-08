import re

i = 0

r1 = '(\w)(.)\1'

def has_hypernet_ABBA(hypernet_sequences):
    for l in hypernet_sequences:
        print(l)
        if ABBA_detector(l): print(l); return True

def ABBA_detector(pattern):
    for i in range(1, len(pattern) - 2): 
        if pattern[i] == pattern[i+1] and pattern[i-1] == pattern[i+2] and pattern[i] != pattern[i+2]: 
            return True

def BAB_detector(hypernets):
    for s in supernets: print(s)
        # Check if bab pattern is there

def ABA_detector(supernets, hypernets):
    for s in supernets:
        aba = re.search('(\w)(\w)\\1', s)
        #aba = re.search('(\w)(\w)\1', s) # in one go: if re.search(regex): BAB_detector(hypernets)
        if aba is not None: print(aba)



with open('small_input') as f: 
    for line in f:
        line = line.strip()
        supernets = re.findall('(\w+?)(?:\[.*?\]|$)', line)
        hypernets = re.findall('\[(\w+?)\]', line)
        print('supernets: {0}'.format(supernets))
        print('hypernets: {0}'.format(hypernets))
        ABA_detector(supernets,hypernets)
        
