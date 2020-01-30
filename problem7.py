"""
In this problem I just use bruteforce until I reach 10001st prime number.
"""

def checkPrime(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0:
            return False
    
    return True

def main():
    number = 3
    nth_prime = 1
    while nth_prime < 10001:
        if checkPrime(number):
            nth_prime += 1
            number += 2
        else:
            number += 2

    print(number - 2)


if __name__ == "__main__":
    main()