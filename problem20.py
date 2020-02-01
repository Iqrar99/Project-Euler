"""
Just compute the factorial then count all digits
"""

def factorial(x):
    if x < 1:
        return 1
    return factorial(x-1) * x

def main():
    a = factorial(100)
    total = 0
    while a > 0:
        total += a%10
        a //= 10

    print(total)

if __name__ == "__main__":
    main()