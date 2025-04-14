random_list = [5, 2, 9, 1, 5, 6]
def sort_list(list):
    flag = True
    while flag:
        flag = False
        for i in range(1 , len(list)):
            if list[i-1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                flag = True

print("Unsorted list:", random_list)
sort_list(random_list)
print("Sorted list:", random_list)                