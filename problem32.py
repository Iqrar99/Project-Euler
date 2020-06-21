"""
2 digits x 3 digits = 4 digits, we can use this information
to construct a pandigital number. Also, some numbers can be
formed from 1 digit x 4 digits = 4 digits.
Store the products in a set. Sum all of them in the end of the program.
"""


def is_pandigital(number: str) -> bool:
    """
    function to check whether a number
    is a pandigital 1-9 or not.
    """

    return True if len(set(list(number))) == 9 and '0' not in number else False

def main():
    collected_products = set()

    # search for 2 digits x 3 digits = 4 digits
    for a in range(10, 100):
        if '0' in str(a):
            continue

        for b in range(100, 1000):
            product = a * b
            if '0' in str(product) or '0' in str(b) or len(str(product)) > 4:
                continue

            combined_numbers = str(a) + str(b) + str(product)
            if is_pandigital(combined_numbers):
                collected_products.add(product)
                print(a, b, product)

    # search for 1 digit x 4 digits = 4 digits
    for a in range(1, 10):
        if '0' in str(a):
            continue

        for b in range(1000, 10000):
            product = a * b
            if '0' in str(product) or '0' in str(b) or len(str(product)) > 4:
                continue

            combined_numbers = str(a) + str(b) + str(product)
            if is_pandigital(combined_numbers):
                collected_products.add(product)
                print(a, b, product)

    answer = sum(list(collected_products))
    print(f"answer : {answer}")

if __name__ == "__main__":
    main()
