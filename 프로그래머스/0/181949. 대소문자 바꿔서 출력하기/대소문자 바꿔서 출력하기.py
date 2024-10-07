str = input()
text = list(str)
idx = 0

for i in str:
    if i.islower():
        text[idx] = i.upper()
    else:
        text[idx] = i.lower()
    idx += 1
    
print(''.join(text))