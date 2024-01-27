# testing buble sort algorithm for linked list
ls = [1, 5, 3, 100, 2, 3, 99, 48]

size = len(ls)
swapped = True

for i in range(size):
    swapped = False
    for j in range(size - i - 1):
        if (ls[j] > ls[j+1]):
            ls[j], ls[j+1] = ls[j+1], ls[j]
            swapped = True
    if (not swapped):
        break

print(ls)
