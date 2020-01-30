"""
We can simplify the equation.
since a² + b² = c² then sqrt(a² + b²) = c.
So, a + b + c = a + b + sqrt(a² + b²).
"""

def main():
    answer = 0
    found = False

    for a in range(1,1000):
        for b in range(1,1000):
            if a != b:
                c = (a**2 + b**2)**0.5
                if a + b + c == 1000:
                    answer = a*b*c
                    found = True
                    break
        if found: break
    
    print(int(answer))

            

if __name__ == "__main__":
    main()