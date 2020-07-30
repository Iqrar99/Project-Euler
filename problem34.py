"""
Don't forget to store all factorials from 0 to 9.
We can save our computation time with it.
"""

def main():
    factorial = [0]*10
    factorial[0] = 1
    factorial[1] = 1
    
    for i in range(2, 10):
        factorial[i] = i*factorial[i-1]

    ans = 0
    for number in range(3, 10**7):
        total = 0
        x = number

        while x != 0:
            total += factorial[x%10]
            x //= 10
        
        if total == number:
            ans += total

    print(ans)

if __name__ == "__main__":
    main()