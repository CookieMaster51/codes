unsorted = [3, 6, 32, 532, 46, 23, 3, 34, 13, 87, 4, 84, 26]

while sorted != True:
    sorted = True
    for i in range(0, len(unsorted) - 1):    
        if unsorted[i] > unsorted[i + 1]:
            unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
            sorted = False
sorted = unsorted

print(sorted)