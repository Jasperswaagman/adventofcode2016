import hashlib
import random
import string

final_pass = ['_', '_', '_', '_', '_', '_', '_', '_']

i = 0
valid_chars = 0
with open('input') as f: door_id = f.read()
door_id = door_id.strip()

while valid_chars < 8:
    id_inc = door_id + str(i)
    hashed_id = hashlib.md5()
    hashed_id.update(id_inc.encode('utf-8'))
    hashed_id = hashed_id.hexdigest()
    if hashed_id.startswith('00000'): 
        position = hashed_id[5]
        if position.isdigit(): 
            position = int(position)
            if position < 8 and final_pass[position] == '_':
                final_pass[position] = hashed_id[6]
                print('Password is: {0}'.format(''.join(final_pass)), end='\r')
                valid_chars += 1
    i += 1

