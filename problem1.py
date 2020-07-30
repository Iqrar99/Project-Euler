"""
We will solve this problem mathematically.
We need to use Inclusive-Exclusive principle.
"""

# function to find Sn in an arithmetic sequence
def Sn(a, b, n):
    return (n*(2*a + (n-1)*b))//2

def main():
    five = Sn(5, 5, 999//5)
    three = Sn(3, 3, 999//3)
    fifteen = Sn(15, 15, 999//15)

    answer = five + three - fifteen
    print(answer)

if __name__ == "__main__":
    main()