"""
First, we need to generate all 4 digits prime numbers. Then greedy
all of them and use permutation to form new numbers. Use binary search
to check if the permutated numbers is in our prime list and include
them in a candidate list.
After that, bruteforce all passed candidates sequences using
3 nested loops since we know the answer will be 12 digits.
"""

from math import sqrt, floor
from itertools import permutations

def is_prime(number) -> bool:
    """
    function to check whether the number is prime or not.
    """
    if number < 2:
        return False

    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def search(target, prime_list) -> bool:
    """
    function to search a number in a list using Binary Search.
    """

    l, r  = 0, len(prime_list) - 1
    while l <= r:
        m = (l + r) // 2
        
        if prime_list[m] == target:
            return True

        elif prime_list[m] < target:
            l = m + 1

        else:
            r = m - 1

    return False

def main():
    prime_list = [n for n in range(1001, 10000, 2) if is_prime(n)]
    candidates = []

    for x in prime_list:
        perm = list(permutations(list(str(x))))
        tmp_numbers = []

        for i in range(len(perm)):
            p = int("".join(list(perm[i])))

            if p % 2 == 0:
                continue
        
            if search(p, prime_list):
                tmp_numbers.append(p)

        tmp_numbers.sort()
        if len(tmp_numbers) >= 3:
            candidates.append(tmp_numbers)
            
    passed = []
    for candidate in candidates:
        length = len(candidate)
        found = False

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if abs(candidate[i] - candidate[j]) == abs(candidate[j] - candidate[k]) \
                    and len(set([candidate[i], candidate[j], candidate[k]])) == 3:
                        passed.append(sorted([candidate[i], candidate[j], candidate[k]]))
                        found = True

                    if found: break
                if found: break
            if found: break

    answer = set()
    for seq in passed:
        answer.add("".join(list(map(str, seq))))

    print("answer :", [x for x in answer])

if __name__ == "__main__":
    main()
