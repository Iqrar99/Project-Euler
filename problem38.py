"""
Start from 9000 to 10000 to check the products that can
produce a pandigital number. Use the set operation to check
the duplicate digits when concatenate the numbers.
"""

def is_pandigital(number : str) -> bool:
    """
    function to check whether a number
    is a pandigital 1-9 or not.
    """

    return True if len(set(list(number))) == 9 and '0' not in number else False

def main():
    answer = 0
    the_number = 0
    
    for number in range(9000, 10000):
        combined_numbers = ""
        product_list = []

        for x in range(1, 10):
            product = str(number * x)
            combined_numbers += product
            product_list.append(x)

            if len(combined_numbers) > 9:
                break
            
            elif len(combined_numbers) == 9 and is_pandigital(combined_numbers):
                if answer < int(combined_numbers):
                    answer = int(combined_numbers)
                    the_number = number
                
                break

    print(f"answer : {answer}")

if __name__ == "__main__":
    main()
