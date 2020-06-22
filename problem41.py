"""
We can use a python library called Sympy.
Generate the prime numbers from 1000000 to 100000000
and check each of them manually from backward.
"""

from sympy import sieve

def is_pandigital(number) -> bool:
    """
    function to check whether a number is pandigital or not.
    """
    digits = list(map(int, list(str(number))))
    maximum_num = max(digits)

    if len(digits) != maximum_num:
        return False

    for i in range(1, maximum_num + 1):
        if i not in digits:
            return False

    return True

def main():
    prime_numbers = reversed(list(sieve.primerange(1000000, 100000000)))

    answer = 0
    for number in prime_numbers:
        if is_pandigital(number):
            answer = number
            break

    print(f"answer : {answer}")

if __name__ == "__main__":
    main()

