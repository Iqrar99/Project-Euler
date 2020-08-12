"""
We need to generate all abundant numbers first.
Then store them into a list.
"""
abundant_list = []

def abundantCheck(n):
    nn = n

    mul = 1
    for p in range(2, n + 1):
        power = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                power += 1
            mul *= (p**(power + 1) - 1) // (p - 1)  # the formula from problem #21
        if n == 1:
            break

    return True if mul - nn > nn else False

def main():
    for i in range(12, 28124):
        if abundantCheck(i):
            abundant_list.append(i)

    total_non_abundant = 0
    total_abundant = 0
    total = (28123 * 28124) // 2

    two_abundant_set = set()

    # let's sum all possible numbers that came from adding 2 abundant numbers
    for a in range(len(abundant_list)):
        for b in range(len(abundant_list)):
            summation = abundant_list[a] + abundant_list[b]
            if (summation) <= 28123 and (summation not in two_abundant_set):
                # print(summation)
                total_abundant += summation
                two_abundant_set.add(summation)

    total_non_abundant = total - total_abundant

    print(total_non_abundant)


if __name__ == "__main__":
    main()
