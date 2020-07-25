"""
Since it will be 19 digits, we can start the bruteforce from 10-digits number.
We know the last digit is zero, so we only need to search the numbers multples of 10.
"""

def check(number: int) -> bool:
    """
    a function to check whether the number is satisfied with the rule or not.
    """

    n = str(number)
    if len(n) == 19:
        if n[0] + n[2] + n[4] + n[6] + n[8] + n[10] + n[12] + n[14] + n[16] + n[18] == '1234567890':
            return True

    return False

def main():
    start = 1010101010
    found = False

    while not found:
        computed = start**2
        start += 10
        found = True if check(computed) else False

    print(f"answer: {start-10}^2 = {computed}")

if __name__ == "__main__":
    main()