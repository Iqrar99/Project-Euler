"""
We can solve this by simplify the formula n/φ(n) to be ∏{p|n}(p/(p-1)).
"""

from math import sqrt, floor

def is_prime(x: int) -> bool:
    """
    function to check whether a number is a prime or not.
    """

    if x < 2:
        return False

    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def main():
    prime_list = [2] + [x for x in range(3, 50, 2) if is_prime(x)]

    i = 0
    result = 1
    max_n = -1

    while result * prime_list[i] <= 10**6:
        result *= prime_list[i]
        i += 1

    print(f"answer : {result}")

if __name__ == "__main__":
    main()
