"""
If a number contains an even number, just ignore it.
"""

def checkPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    return True

def containsEven(x):
    for n in str(x):
        if int(n) % 2 == 0:
            return True

    return False

def circularPrimes(number):
    n = str(number)
    for _ in range(len(n)):
        if not checkPrime(int(n)):
            return False
        else:
            n = n[1:] + n[0]

    return True


def main():
    ans = 1

    # just check all odd numbers
    for number in range(3, 10**6, 2):
        if not containsEven(number):
            ans += 1 if circularPrimes(number) else 0

    print(ans)

if __name__ == "__main__":
    main()