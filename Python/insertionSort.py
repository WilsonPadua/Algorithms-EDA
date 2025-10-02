input = [0, 1, 3, 4, 6, 7]

def insertionSort(num, list):
    input.append(num)
    for i in range(len(list) -1, 0, -1):
        if (list[i] < list[i -1]):
            list[i], list[i-1] = list[i-1], list[i]

insertionSort(2, input)
insertionSort(8, input)

print(input)
            
