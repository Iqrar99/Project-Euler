"""
This problem needs a good implementation.
"""

def checkPrime(x):
    if x != 1:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
    else:
        return False

    return True

def truncatable(x):
    num = str(x)
    for _ in range(len(num)):
        if not checkPrime(int(num)):
            return False
        else:
            num = num[1:]

    num = str(x)
    for _ in range(len(num)):
        if not checkPrime(int(num)):
            return False
        else:
            num = num[:-1]

    return True

def main():
    ans = 0
    for number in range(11, 10**6, 2):
        if truncatable(number):
            ans += number

    print(ans)


if __name__ == "__main__":
    main()
