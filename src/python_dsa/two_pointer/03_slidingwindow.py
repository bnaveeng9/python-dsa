def longest_substring_without_repeating_characters(arr: str) -> int:
    if len(arr)<=0:
        return 0
    
    l,r = 0,0
    longest_substring_len = 0

    window = set()

    for r in range(len(arr)):
        if arr[r] in window:
            window.remove(arr[l])
            l+=1
        window.add(arr[r])
        longest_substring_len = max( longest_substring_len, (r-l)+1 )

    return longest_substring_len

        

def main():
    arr = "abccabc"
    l = longest_substring_without_repeating_characters(arr)
    print(f"longest_substring_without_repeating_characters for string :{arr} is : {l}")

    arr = "aaaabaaa"
    l = longest_substring_without_repeating_characters(arr)
    print(f"longest_substring_without_repeating_characters for string :{arr} is : {l}")
    
if __name__ == "__main__":
    main()

        
        
        




