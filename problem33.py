"""
Suppose that n, m, and k is a number representation.
The non-trivial examples can be found if and only if
nm/mk = n/k then (nm/mk) / (n/k) = 1.
Bruteforce to get the answer.
"""

def check_similar_number(n, d) -> (int, bool):
    """
    function to check a number that appears in
    numerator and denominator.
    """
    
    num = str(n)
    den = str(d)
    uniques = set(num + den)
    total_similar = 0
    answer = 0

    for u in uniques:
        if (u in num) and (u in den):
            total_similar += 1
            answer = int(u)

    if total_similar == 1:
        return answer, True

    return 0, False

def simplify(n, d, similar) -> (int, int):
    """
    function to cancel the similar number from
    numerator and denominator.
    """
    s = str(similar)
    num = str(n).replace(s, "", 1)
    den = str(d).replace(s, "", 1)

    return int(num), int(den)

def GCD(a, b) -> int:
    """
    function to find the Greatest Common Divisor from
    two numbers using Euclidean Algorithm.
    """

    if a == 0:
        return b

    return GCD(b % a, a)

def main():
    simplified_numerator = []
    simplified_denominator = []

    for i in range(1, 10):
        for j in range(i + 1, 10):
            simplified_numerator.append(i)
            simplified_denominator.append(j)

    nontrivia_numerator = []
    nontrivia_denominator = []

    for numerator in range(11, 100):
        for denominator in range(numerator + 1, 100):
            similar_number, status = check_similar_number(
                numerator, denominator)

            if status and (similar_number != 0):
                num, den = simplify(
                    numerator, denominator, similar_number)

                try:
                    x = (numerator/denominator) / (num/den)
                    if x == 1.0:
                        nontrivia_numerator.append(numerator)
                        nontrivia_denominator.append(denominator)
                
                except ZeroDivisionError as z:
                    continue

    print(*nontrivia_numerator)
    print(*nontrivia_denominator)

    product_num = 1
    product_den = 1
    for i in range(len(nontrivia_numerator)):
        product_num *= nontrivia_numerator[i]
        product_den *= nontrivia_denominator[i]

    divisor = GCD(product_num, product_den)
    answer = product_den // divisor

    print(answer)


if __name__ == "__main__":
    main()
