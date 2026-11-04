def sum_of_two_numbers_to_target(arr: list[int], target : int ) -> ( int,int):
    if len(arr) <=0:
        return (0,0)
    arr.sort()

    left = 0
    right: int = (len(arr) -1)
    right = right -1
    print(f"length of left: {left} and right :{right}")
    print(f" left: {arr[left]} and rights :{arr[right]}")

    while left <= right:
        l = arr[left] 
        r = arr[right]
        total = l + r
        if arr[left]+arr[right] == target:
            return (left, right)
        if  arr[left]+arr[right] < target:
            left+=1
        elif  arr[left]+arr[right] > target:
            right-=1
        
    return (-1, -1)

    

def stub_sum_of_two_numbers_to_target(arr:list[int], target: int):
    
    (l,r) = sum_of_two_numbers_to_target(arr, target)
    if (l,r) == (-1,-1):
        print("not found")
    else:
        print(f"sum of {arr[l]} + {arr[r]} is equal : {target}")
        print(f"index of {l} + {r}")

        
if __name__ == "__main__":
    arr: list[int] = [x for x in range(1,11)]


    stub_sum_of_two_numbers_to_target(arr, 8)
    stub_sum_of_two_numbers_to_target(arr, 4)
    stub_sum_of_two_numbers_to_target(arr, 6)