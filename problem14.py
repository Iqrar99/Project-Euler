"""
Bruteforce!
"""

def main():
    longest = -1
    answer = 0
    for n in range(999999, 1, -1):
        counter = 0
        x = n
        while x != 1:
            x = x // 2 if x % 2 == 0 else 3 * x + 1
            counter += 1

        if counter > longest:
            longest = counter
            answer = n
    
    print(answer)


if __name__ == "__main__":
    main()