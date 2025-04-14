password = "password"
login = input("Enter password: ")
while login != password:
    print("Incorrect password")
    login = input("Enter password: ")
print("Correct password")