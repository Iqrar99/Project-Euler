"""
Bruteforce is the general idea.
In this problem, we need to multiply all the power from prime factors of a number.
So the formula will be like:
    divisor = (p_power₁ + 1) * (p_power₂ + 1) * ... * (p_powerₙ + 1)
"""

def checkPrime(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0:
            return False

    return True


def main():
    triangle_number = 0
    counter = 1

    while True:
        triangle_number += counter
        t_tmp = triangle_number
        counter += 1
        mul = 1

        for i in range(2, int(triangle_number**0.5)+1):
            if checkPrime(i):
                power_counter = 0
                while t_tmp % i == 0:
                    t_tmp //= i
                    power_counter += 1
                mul *= (power_counter + 1)

                if t_tmp == 1: break

        divisor = mul
        # print(triangle_number, divisor)  <-- DEBUG

        if divisor > 500:
            print(triangle_number)
            break

if __name__ == "__main__":
    main()
