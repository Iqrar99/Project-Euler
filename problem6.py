"""
We can use arithmetic sequence formula to find Sn.
"""

def Sn(a, b, n):
    return n * (2 * a + (n - 1) * b) // 2

def main():
    square_of_sum = Sn(1, 1, 100)**2
    sum_of_square = (100 * 101 * 201) // 6  # using sum of square sequence formula 

    print(square_of_sum - sum_of_square)

if __name__ == "__main__":
    main()