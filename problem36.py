"""
Create a recursive method to check if a number is palindrome or not.
"""

def checkPalindrome(s):
    if len(s) < 2:
        return True 
    
    if s[0] != s[-1]:
        return False
    else:
        return checkPalindrome(s[1:-1])

def main():
    total = 0

    for number in range(1,10**6):
        binary = int(bin(number)[2:])

        if checkPalindrome(str(number)):
            if checkPalindrome(str(binary)):
                total += number

    print(total)

if __name__ == "__main__":
    main()