n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    lst.append(input("Enter the element: "))
str = ",".join(lst)
print(str)
print(type(str))