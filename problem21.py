"""
Let's use a formula to calculate the sum of all divisiors of a number
"""

def d(n):
    nn = n

    mul = 1
    for p in range(2, n+1):
        power = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                power += 1
            mul *= (p**(power+1) - 1)//(p-1) # the formula
        if n == 1: break

    return mul - nn

def main():
    total = 0
    for a in range(2, 10000):
        b = d(a)
        c = d(b)
        if c == a and a != b:
            total += a

    print(total)


if __name__ == "__main__":
    main()

