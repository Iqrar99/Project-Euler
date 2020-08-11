"""
The easiest way is storing all numbers that will touch number 1 and 89.
That way, we just check all numbers stored before for the rest.
"""

# a useful library to show progress bar during iteration
from tqdm import tqdm

def calculate(x: int) -> int:
    """
    function to add the square of the digits in a number.
    """

    digits = list(map(int, list(str(x))))
    return sum(list(map(lambda a: a**2, digits)))

def main():
    history_1 = {1: 1}
    history_89 = {89: 89}

    for number in tqdm(range(2, 10**7)):
        try:
            get = history_1[number]
            continue
        
        except KeyError:
            try:
                get = history_89[number]
                continue

            except KeyError:
                x = number
                history = []
                while x not in [1, 89]:
                    history.append(x)
                    x = calculate(x)

                if x == 1:
                    history_1.update(dict(zip(history, history)))
                else:
                    history_89.update(dict(zip(history, history)))

    print(f"answer : {len(history_89)}")


if __name__ == "__main__":
    main()