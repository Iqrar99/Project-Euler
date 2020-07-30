"""
In this problem, I'll use a powerful python library: itertools.
Just import permutations and give a list of number to get the permutation
"""

from itertools import permutations

def main():
    perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(list(perm)[999999])

if __name__ == "__main__":
    main()