import string
import random
first = ':'.join(random.choices(string.hexdigits , k=12))
splited = first.split(':')
i = -1
second = ''
for char in splited:
    i += 1
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        second += char + ':'
    else:
        second += char
print(second)

    