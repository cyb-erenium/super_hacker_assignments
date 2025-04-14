for i in range (9999):
    if i < 10:
        print("000" + str(i))
    elif i < 100:
        print("00" + str(i))
    elif i < 1000:
        print("0" + str(i))
    else:
        print(i)