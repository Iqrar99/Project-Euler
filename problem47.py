"""
First, we need to save all prime numbers below 1000 since we know
that a number < 1000000 is impossible has a prime factor more than 1000.
Then, use greedy technique to search the first four consecutive numbers
that have four distinct prime factors.
"""

from math import sqrt, floor

def is_prime(number) -> bool:
    if number < 2 :
        return False

    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def get_total_factors(number, prime_list) -> list:
    """
    function to produce all prime factors from a number.
    """

    if is_prime(number):
        return [number]

    factor_list = []

    for prime in prime_list:
        if number % prime == 0:
            factor_list.append(prime)

    return factor_list

def main():
    prime_list = [x for x in range(2, 1000) if is_prime(x)]

    prime_factors = {}
    start = 0
    target = 0
    answer = []
    for number in range(1000, 10**6):
        prime_factors[number] = get_total_factors(number, prime_list)

        if len(prime_factors[number]) == 4:
            start = number if start == 0 else start
            target += 1
            answer.append(number)

        else:
            start = 0
            target = 0
            answer.clear()

        if target == 4:
            break

    print(f"answer : {answer}")

if __name__ == "__main__":
    main()