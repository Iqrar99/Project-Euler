"""
We need to iterate all numbers and append it into a string variable.
Do it until the length of the string variable > 1000000.
"""

def main():
    numbers = ''
    i = 1
    while len(numbers) <= 1e6:
        numbers += str(i)
        i += 1

    idx = [1, 10, 100, 1000, 10000, 100000, 1000000]
    answer = 1
    for n in idx:
        answer *= int(numbers[n - 1])

    print(answer)

if __name__ == "__main__":
    main()
