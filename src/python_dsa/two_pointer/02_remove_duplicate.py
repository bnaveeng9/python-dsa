'''
The both pointer move in same direction. slow = 0 and fast =1
fast scans the list 
    1. if slow == fast then move fast
    2. if slow != fast 
        then move slow 
        then copy fast to slow
        move fast
    3. repeat 1,2 until fast hits the end of list 
    4, unique elements will appear in the fornt
'''
def remove_duplicates_in_list(arr: list[int] ) -> index:
    if len(arr) <=0:
        return 0
    arr.sort()

    slow = 0 
    fast = 1

    while fast < len(arr):
        if arr[slow] == arr[fast]:
            arr[slow] = arr[fast]
            fast+=1
        elif arr[slow] != arr[fast]:
            slow+=1
            fast+=1
    return slow


def remove_duplicates_in_list_2(arr: list[int] ) -> index:
    if len(arr) <=0:
        return 0
    arr.sort()

    slow = 0 
    fast = 0

    for  fast in range( len(arr)):
        if arr[slow] != arr[fast]:
            slow+=1
            arr[slow] =arr[fast]
    return slow+1



def stub_remove_duplicates_in_list(arr:list[int]):
    
    index = remove_duplicates_in_list_2(arr)
    if index <=0:
        print("not found")
    else:
        print(f"index found at :{index}")
        for x in range(index):
            print(x)


if __name__ == "__main__":
    arr: list[int] = [0,0,0,1,2,3,1,2,3,1,2,3,4]
    stub_remove_duplicates_in_list(arr)

    arr : list[int] = [0,0,1,1,1,2,2]
    stub_remove_duplicates_in_list(arr)
    