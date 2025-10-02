input = [1,2,3,4,5,6,7,8,9,10]
target = 20

def binarySearch(input, target):
    left, rigth = 0, len(input) -1

    while(left <= rigth):
        mid = (left + rigth) // 2
        if (input[mid] == target):
            return mid
        elif (target < input[mid]):
            rigth = mid -1
        else:
            left = mid + 1
        
    return -1

print(binarySearch(input, target))