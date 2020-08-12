"""
To make the computation faster, we need to do arithmetic approach first.
- a^2 + b^2 = c^2   (1)
- a + b + c = p     (2)

we can rewrite them as
c = p - a - b
a^2 + b^2 = (p - a - b)^2 = p^2 +a^2 + b^2 - 2pa -2pb -2ab
b = p(p - 2a) / 2(p - a)
"""

def main():
    result = 0
    answer = 0

    for p in range(2, 1001, 2):
        number_of_solution = 0
        for a in range(2, p // 3):
            if (p * (p - 2 * a) % (2 * (p - a))) == 0:
                number_of_solution += 1
            
            if number_of_solution > result:
                result = number_of_solution
                answer = p

    print(f"answer : {answer}")

if __name__ == "__main__":
    main()

