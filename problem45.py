"""
Iterate the triangle, pentagonal, and hexagonal numbers
and save them in different sets. Then, union all of them.
"""

def main():

    triangle_numbers = set()
    for n in range(1, 10**5):
        x = (n * (n + 1)) // 2
        triangle_numbers.add(x)

    pentagonal_numbers = set()
    for n in range(1, 10**5):
        x = (n * (3 * n - 1)) // 2
        pentagonal_numbers.add(x)

    hexagonal_numbers = set()
    for n in range(1, 10**5):
        x = n * (2 * n - 1)
        hexagonal_numbers.add(x)

    special = triangle_numbers.intersection(
        pentagonal_numbers.intersection(hexagonal_numbers))
    special = sorted(list(special))
    
    print(*special)

if __name__ == "__main__":
    main()