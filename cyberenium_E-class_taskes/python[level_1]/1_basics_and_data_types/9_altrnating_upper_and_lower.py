s = 'H4ck3r'
ss = ""
for letter in s:
    if letter.isupper():
        ss += (letter.lower())
    elif letter.islower():
        ss += (letter.upper())
    else:
        ss += (letter)
print(f"{s} => {ss}")              