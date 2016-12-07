import re
# --- Day 7: Internet Protocol Version 7 ---
# 
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
# 
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
# 
# For example:
# 
# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
# How many IPs in your puzzle input support TLS?

i = 0

def ABBA_detector(pattern):
    for i in range(len(pattern) - 1): 
        if pattern[i] == pattern[i+1] and pattern[i-1] == pattern[i+2] 
            and pattern[i+1] != pattern[i+2]: return True # We need to add a check so aaaa is invalid


with open('small_input') as f: 
    for line in f:
        print(line)
        r = re.findall('(\[.*?\])', line) # Need to get all the bracket groups and join them, then the rest
        print(r)
        for _ in r: # Need to go over all the lists in r
            print(_)
            if ABBA_detector(_): break
        #if ABBA_detector(bracket_part): break
        #if ABBA_detector(rest): i += 1

print(i)
        
