"""
In this problem we need to iterate the fibonacci numbers
and calculate the answer at the same time.
"""

def main():
    answer = 0
    a, b = 1, 2

    while b <= 4*10**6:
        answer += b if (b % 2 == 0) else 0
        a, b = b, a+b

    print(answer)


if __name__ == "__main__":
    main()