n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    lst.append(input("Enter the element: "))
for j in lst:
    for k in lst:
        if j == k:
            lst.remove(j)
print("The list after removing duplicates is:", lst)
