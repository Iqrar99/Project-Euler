"""
We need to work this problem by using I/O in python
"""

def compute(s):
    value = 0
    for letter in s:
        value += ord(letter) - 64
    
    return value

def main():
    with open('p022_names.txt', 'r') as infile:
        data = infile.read().split(',')

    for i in range(len(data)):
        data[i] = data[i].replace('"', '')

    data.sort()

    total = 0
    for i in range(len(data)):
        total += (i + 1) * compute(data[i])

    print(total)

if __name__ == "__main__":
    main()