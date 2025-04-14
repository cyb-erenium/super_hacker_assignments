import re
def password_check(password):
    #variables
    check_one = False
    check_two =  False
    check_three = False
    #length check
    if len(password) < 8:
        check_one = False 
    else: 
        check_one = True
    #number check    
    if re.search(r'[1-9]', password):
        check_two = True
    else:
        check_two = False
    #special character check
    if re.search(r'[!@#$%^&*()_.,?/><+=-]',password):
        check_three = True
    else:
        check_three = False
    return check_one, check_two, check_three
# Main program    
passwrd = input("Enter a password: ")
check_one, check_two, check_three = password_check(passwrd)
if check_one == True and check_two == True and check_three == True:
    print("Password is strong")
else:
    print("Password isn't strong enough")
    print("Password must be at least 8 characters long, contain at least one number, and contain at least one special character.")
    while True:
        passwrd = input("Enter a password: ")
        check_one, check_two, check_three = password_check(passwrd)
        if check_one == True and check_two == True and check_three == True:
            print("Password is strong")
            break
        else:
            print("Password isn't strong enough")
            print("Password must be at least 8 characters long, contain at least one number, and contain at least one special character.")




            