
def selection_sort(arr : List[int]) -> List[int]:
    min_index = -1
    for i in range(len(arr)):
        min = arr[i] 
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                min = arr[j]
            print(f"min {min}, min_index {min_index}")
        # temp = arr[i]
        # arr[i] = min
        # arr[min_index]= temp
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr : List[int]) -> List[int]:

    isSwapped = False
    while True:
        isSwapped = False
        print ("start ")
        for i in range( 1, len(arr)):
            #print (f"before first : {arr[i-1]} second: {arr[i]} ")
            if arr[i] < arr[i-1]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
               #print (f"After first : {arr[i-1]} second: {arr[i]} ")
                isSwapped = True
        if not isSwapped:
            return arr
        # else:
        #     continue
        
    return arr

         
if __name__ == "__main__":
    arr: list[int] = [1,5,3,4,2,6]
    res = selection_sort(arr)
    #res = bubble_sort(arr)
    print (res)

    # arr = [x for x in range(12)]
    # res = bubble_sort(arr)
    # print (res)
    #print(" ".join(map(str, res)))

                