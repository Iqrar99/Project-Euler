"""
Find all results and store it in a set.
"""

def main():
    result  = set()
    for a in range(2, 101):
        for b in range(2, 101):
            result.add(a**b)
    
    print(len(result))

if __name__ == "__main__":
    main()