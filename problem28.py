#
"""
based on the problem, we should approach a formula for each diagonals

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

1   7   21  43  73  ...
U(n) = 8n - 10 + U(n-1), with n > 1

1   3   13  31  57  ...
U(n) = 8n - 14 + U(n-1), with n > 1

1   9   25  49  81  ...  
U(n) = (2n - 1)^2

1   5   17  37  65  ...
U(n) = 4(n-1)^2 + 1
"""


def d1(n):
    a = 1
    total = 1
    for i in range(2, n+1):
        a = 8*i - 10 + a
        total += a

    return total


def d2(n):
    a = 1
    total = 1
    for i in range(2, n+1):
        a = 8*i - 14 + a
        total += a

    return total


def d3(n):
    total = 0
    for i in range(1, n+1):
        total += (2*i - 1)**2

    return total


def d4(n):
    total = 0
    for i in range(1, n+1):
        total += 4*(i-1)**2 + 1

    return total


def main():
    x = 1001//2 + 1

    print(d1(x) + d2(x) + d3(x) + d4(x) - 3)


if __name__ == "__main__":
    main()
