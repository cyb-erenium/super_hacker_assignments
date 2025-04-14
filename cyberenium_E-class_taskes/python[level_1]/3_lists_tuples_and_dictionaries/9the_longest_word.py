bigger = ""
n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    lst.append(input("Enter the element: "))
for j in lst:
    for k in lst:
        if len(j) > len(k):
            bigger = j
        else:
            bigger = k
print("The longest word is:", bigger)            
