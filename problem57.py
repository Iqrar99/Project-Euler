"""
We can solve this problem using sliding window. Construct the function to
calculate the fraction first.
"""

def calculate(n, d):
    """
    function to calculate the fractions.
    """

    return d, (2 * d) + n

def main():
    cnt = 0
    numerator = 1
    denominator = 2
    
    for i in range(1, 1000):
        numerator, denominator = calculate(numerator, denominator)
        result = (numerator + denominator, denominator)
 
        if len(str(result[0])) > len(str(result[1])):
            cnt += 1

    print(f"answer: {cnt}")

if __name__ == "__main__":
    main()
