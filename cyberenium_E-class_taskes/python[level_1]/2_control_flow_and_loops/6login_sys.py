password = 'password'
attempts = 0
for i in range(3):
    user_input = input('Enter password: ')
    if user_input == password:
        print('successful login')
    else:
        attempts += 1
        print(f'Incorrect password, {3 - attempts} attempts left')