"""
We can solve it using bruteforce.
"""

def is_palindrome(number: str) -> bool:
    """
    function to check whether the number is a palindrome or not.
    """
    
    if len(number) <= 1:
        return True
    
    if number[0] != number[-1]:
        return False

    return is_palindrome(number[1:-1])
    

def main():
    lychrel_cnt = 0

    for n in range(10, 10000):
        x = n
        for i in range(49):
            x = x + int(str(x)[::-1])
            if is_palindrome(str(x)):
                break

        else:
            lychrel_cnt += 1

    print(f"answer : {lychrel_cnt}")

if __name__ == "__main__":
    main()
