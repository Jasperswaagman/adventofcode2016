import hashlib

password = []

i = 0
with open('input') as f: door_id = f.read()
door_id = door_id.strip()

#while not hash_found:
while len(password) < 8:
    id_inc = door_id + str(i)
    hashed_id = hashlib.md5()
    hashed_id.update(id_inc.encode('utf-8'))
    hashed_id = hashed_id.hexdigest()
    if hashed_id.startswith('00000'): 
        password.append(hashed_id[5])
        print('the {0}th char found: {1}'.format(len(password), password[-1]))
    i += 1

print('Password is: {0}'.format(''.join(password)))
