def binary_search(arr: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

def binary_search_duplicate(arr: list[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return boundary_index
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
            
        else:
            left = mid + 1
            boundary_index = mid


    return boundary_index
                        

        # if l<r:
        #     if arr[l+1] > target:
        #         return l
        #     else:
        #         if r+2 <= len(arr)-1:
        #             if arr[r+2] > target:
        #                 return r+2



def stub_duplicate(l: List[int], target : int):
    index = binary_search_duplicate(l, target)
    print(f" {index}")


def stub(l: List[int], target : int):
    index = binary_search_duplicate(l, target)
    print(f" {index}")



if __name__ == "__main__":
    #l = range(1,100)
    l = [1, 3, 3, 5, 8, 8, 10]
   

    stub(l, 2)

    l =  [2, 3, 5, 7, 11, 13, 17, 19]
    stub(l, 6)

    l = [1, 3, 3, 3, 6, 10, 10, 10, 100]
    stub_duplicate(l, 3)