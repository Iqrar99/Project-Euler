"""
We only need to bruteforce.
"""

def main():
    idx = 2
    a = 1
    b = 1

    while len(str(b)) != 1000:
        a, b = b, a + b
        idx += 1

    print(idx)

if __name__ == "__main__":
    main()