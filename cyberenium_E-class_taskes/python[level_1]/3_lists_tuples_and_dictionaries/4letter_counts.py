s = input("Enter a string: ")
c = input("enter a character: ")
count = 0
for i in s:
    if i == c:
        count += 1
print(f"The character '{c}' appears {count} times in the string '{s}'.")