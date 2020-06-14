"""
We only need to bruteforce and check the digits.
"""

def check_digit(x, number) -> bool:
    new_x = int("".join(sorted(list(str(x)))))
    new_number = int("".join(sorted(list(str(number)))))

    return True if new_x ^ new_number == 0 else False

def main():
    for number in range(10, 10**6):
        same = True
        
        for m in range(2, 7):
            x = number * m
            same = check_digit(x, number)

            if not same: break

        if same:
            print(f"answer: {number}")
            break


if __name__ == "__main__":
    main()
