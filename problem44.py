"""
First, generate the pentagon numbers. Use bruteforce to get
a pair of number and use the binary search to check whether a number
is a pentagon or not.
"""

def pentagon(n) -> int:
    """
    function to produce a pentagon number.
    """

    return (n * (3*n - 1)) // 2

def search(x, pentagon_list) -> bool:
    """
    function to perform binary search.
    """
    l = 0
    r = len(pentagon_list) - 1

    while l <= r:
        m = (l + r) // 2
        if x == pentagon_list[m]:
            return True

        elif x < pentagon_list[m]:
            r = m - 1

        else:
            l = m + 1
    
    return False

def main():
    pentagon_list = [pentagon(n) for n in range(1, 10000)]

    minimum_diff = float('inf')
    the_a_number = 0
    the_b_number = 0
    for i in range(0, len(pentagon_list)):
        a = pentagon_list[i]

        for j in range(i + 1, len(pentagon_list)):
            b = pentagon_list[j]
            c = a + b
            
            if search(c, pentagon_list):
                d = abs(a - b)
                
                if search(d, pentagon_list):
                    if d < minimum_diff: 
                        minimum_diff = d
                        the_a_number = a
                        the_b_number = b

    # may take some times since the complexity is O(n^2(log N))
    print(f'answer : {the_a_number} {the_b_number} -> {minimum_diff}')

if __name__ == "__main__":
    main()