import re

def BAB_detector(aba, hypernets):
    bab = aba[1] + aba[0] + aba[1]
    if any(bab in s for s in hypernets): return True

def ABA_detector(supernets, hypernets):
    global i
    for s in supernets:
        x = 0
        aba_list = []
        for x in range(len(s) - 2): 
            if s[x] == s[x+2] and s[x] != s[x+1]: 
                aba_list.append(s[x] + s[x+1] + s[x+2])
        if aba_list is not None: 
            for aba in aba_list:
                if BAB_detector(aba, hypernets): i += 1; break



with open('input') as f: 
    for line in f:
        line = line.strip()
        supernets = re.findall('(\w+?)(?:\[.*?\]|$)', line)
        hypernets = re.findall('\[(\w+?)\]', line)
        ABA_detector(supernets,hypernets)
        
print(i)
