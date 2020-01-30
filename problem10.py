"""
Bruteforce!
"""


def checkPrime(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0:
            return False

    return True

def main():
    total = 2
    number = 3
    while number < 2*10**6:
        if checkPrime(number):
            total += number
        number += 2

    print(total)

if __name__ == "__main__":
    main()
