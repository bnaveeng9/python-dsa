def fizz_buzz(n: int) -> list[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    flist = []
    for x in range(1, n):
        if x%15 == 0 :
            flist.append("FizzBuzz")
        elif x/3 == 0 :
            flist.append("Fizz")
        elif x%5==0:
            flist.append("Buzz")
        else:
            flist.append(str(x))

    return flist

        
if __name__ == "__main__":
    res = fizz_buzz(20)
    print(res)
