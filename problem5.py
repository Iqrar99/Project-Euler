"""
We can solve this problem using LCM.
Remember!
a * b = GCD(a,b) * LCM(a,b)

So we need to find the LCM(1,2,...,20)
"""

# we will use euclidian method
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    return (a * b)//GCD(a, b)

def main():

    lcm = 1
    for i in range(2, 21):
        lcm = LCM(lcm, i)

    print(lcm)

if __name__ == "__main__":
    main()
