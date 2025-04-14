import hashlib
txt = input("Enter the text to hash: ")
hashed_txt = hashlib.md5(txt.encode()).hexdigest()
print(f"MD5 hash of '{txt}' is: {hashed_txt}")