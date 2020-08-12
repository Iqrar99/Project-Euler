"""
Just brute force all 3-digit numbers.
"""

def checkPalindrome(n: str):
    if len(n) > 1:
        if n[0] == n[-1]:
            return checkPalindrome(n[1:-1])
        else:
            return False
    else:
        return True
        

def main():
    max_palindrome = 0

    for a in range(100, 1000):
        for b in range(100, 1000):
           mul = a * b
           if checkPalindrome(str(mul)):
               max_palindrome = max(max_palindrome, mul)

    print(max_palindrome)

if __name__ == "__main__":
    main()