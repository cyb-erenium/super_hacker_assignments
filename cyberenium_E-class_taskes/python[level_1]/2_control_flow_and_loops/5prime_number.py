prime = int(input("Enter a number: "))
if prime == 2 or prime == 3:
    print(prime, "is a prime number.")
elif prime % 2 == 0 or prime % 3 == 0:
    print(prime, "is not a prime number.")
else:
    print(prime, "is a prime number.")