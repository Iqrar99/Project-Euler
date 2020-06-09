"""
Generate the triangle numbers sequence until maximum value from
`words.txt` file. Then use greedy technique to check each words.
"""

def triangle_number(n) -> int:
    return n * (n + 1) // 2

def get_alphabet_value() -> dict:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = [s for s in ALPHABET]

    return dict(zip(alphabet, list(range(1, 27))))

def generate(constraint) -> set:
    """
    function to generate the triangle numbers sequence.
    """
    seq = set()
    n = 1
    number = triangle_number(n)

    while number <= constraint:
        seq.add(number)
        n += 1
        number = triangle_number(n)

    return seq

def get_value(word, alphabet_value) -> int:
    value = 0
    for w in word:
        value += alphabet_value[w]

    return value

def main():
    alphabet_value = get_alphabet_value()

    with open('p042_words.txt') as infile:
        WORDS = infile.read().replace('"', '').split(',')

    max_length = max(map(len, WORDS))
    constraint = 26 * max_length

    seq = generate(constraint)    

    count = 0
    for word in WORDS:
        value = get_value(word, alphabet_value)
        count = count + 1 if value in seq else count

    print(count)

if __name__ == "__main__":
    main()