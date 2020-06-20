"""
First, generate all pandigital numbers using permutation.
Then, check each of them.
"""

from itertools import permutations

def check(number) -> bool:
    """
    function to check whether the number is satisfied
    all properties or not.
    """
    primes = [2, 3, 5, 7, 11, 13, 17]

    for i in range(1, 8):
        x = int(number[i:i+3])

        if x % primes[i - 1]:
            return False

    return True

def main():
    numbers = list('0123456789')
    pandigital_numbers = list(permutations(numbers))
    total = 0

    for n in pandigital_numbers:
        number = "".join(list(n))
        
        if check(number):
            total += int(number)
            print(number)

    print(f"answer: {total}")


if __name__ == "__main__":
    main()