"""
Use bruteforce to find the twice a square number then subtract
a number we iterated before with that number. After that, check if
the result is a prime number or not.
"""

from math import sqrt, floor

def is_prime(n) -> bool:
    """
    a function to check wether a number is a prime number or not.
    """
    if n < 2:
        return False

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def main():

    # use dict to make it O(1)
    prime_numbers = dict()
    for number in range(2, 10000):
        if is_prime(number):
            prime_numbers[number] = number
    
    two_twice_square = []
    for number in range(1, 260):
        two_twice_square.append(2*number**2)

    for x in range(35, 10000, 2):
        if x not in prime_numbers:
            result = False

            for number in two_twice_square:
                if number < x:
                    y = x - number
                    
                    try:
                        prime = prime_numbers[y]
                        result = True
                        print(f"{x} = {prime} + 2*{floor(sqrt(number//2))}^2")
                        break

                    except KeyError as k:
                        pass

            if not result:
                print(f"answer: {x}")
                break

if __name__ == "__main__":
    main()