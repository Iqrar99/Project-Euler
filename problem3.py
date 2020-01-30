"""
Since we know the number in this problem is odd.
We can iterate every odd number from 3 to sqrt(number).
"""

def main():
    number = 600851475143
    max_prime_factor = 1

    for i in range(3, int(number**(0.5)) + 1, 2):
        if number % i == 0:
            max_prime_factor = i
            while (number % i == 0):
                number //= i

        if number == 1: break

    print(max_prime_factor)

if __name__ == "__main__":
    main()
