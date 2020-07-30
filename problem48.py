"""
Use modulo as well.
"""

def main():
    ans = 0
    for i in range(1, 1001):
        ans += (i**i) % (10**10)

    print(ans % 10**10)

if __name__ == "__main__":
    main()