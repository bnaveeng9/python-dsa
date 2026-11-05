import math

def binary_search(arr: list[int], target: False) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if len(arr)<=0:
        return -1
    if (len(arr) ==1):
        return 0
    if arr[1] == target:
        return 1
    elif arr[0] == target:
        return 0
    
    l,r = 0, len(arr)-1

    while l<r:
        mid = int(l + (r-l)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid +1
        elif arr[mid] > target:
            r = mid -1
    return -1

if __name__ == "__main__":
    #l = [ 0 for x in range(8) ] + [ 0 for x in range(4) ] + [ 1 for x in range(6) ]
    l = [ 0 for x in range(4) ] + [ 1 for x in range(4) ] + [ 1 for x in range(2) ]
    index = binary_search(l, 1)
    print(f" {index}")
