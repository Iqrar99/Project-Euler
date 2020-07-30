"""
Bruteforce!
"""


def checkPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False

    return True

def main():
    max_a = max_b = -1000
    total_max = -1
    for a in range(-999, 1000):
        for b in range(-999, 1001, 2):
            total = 0
            for n in range(10000):
                formula = n**2 + a*n + b
                if checkPrime(formula):
                    total += 1
                else:
                    break

            if total > total_max:
                total_max = total
                max_a = a
                max_b = b

    # print(max_a, max_b, total_max)
    print(max_a*max_b)


if __name__ == "__main__":
    main()