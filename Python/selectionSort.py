input = [7, 3, 5, 9, 4, 2, 1, 0, 6, 8]

def selectionSort(input):
    for i in range(0, len(input)):
        idxMenor = i
        for j in range(i + 1, len(input)):
            if(input[j] < input[idxMenor]):
                idxMenor = j
        input[i], input[idxMenor] = input[idxMenor], input[i]

selectionSort(input)

print(input)
