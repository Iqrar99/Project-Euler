"""
First of all, we need to generate all prime numbers
from 2 to the closest prime number with 1000000.
Then, use the sliding window technique to get the answer.
"""

from math import sqrt, floor

def is_prime(x) -> bool:
    """
    function to check wether a number is a prime or not.
    """

    if x < 2:
        return False

    for n in range(2, floor(sqrt(x)) + 1):
        if x % n == 0:
            return False

    return True

def main():
    prime_list = [2] + [x for x in range(3, 10**6, 2) if is_prime(x)]

    cumulative_sum = []
    tmp = 0
    for x in prime_list:
        tmp += x
        if tmp < 10**6:
            cumulative_sum.append(tmp)
        else:
            break

    upper_limit_idx = 0
    for i in range(len(prime_list)):
        if prime_list[i] < 10**6:
            upper_limit_idx = i
        else:
            break

    max_count = -1
    answer = 0
    for number in reversed(cumulative_sum):
        count_prime = cumulative_sum.index(number) + 1

        if not is_prime(number):
            tmp = number
            
            for i in range(upper_limit_idx):
                count_prime -= 1
                tmp -= prime_list[i]

                if is_prime(tmp) or tmp < 0: break

        if max_count < count_prime:
            max_count = count_prime
            answer = tmp    

    print(f"answer : {answer}")

if __name__ == '__main__':
    main()
