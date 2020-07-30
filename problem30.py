"""
Just try all numbers as much as possible.
"""

# I just wanna make it O(1) instead of O(n)
def fifthPower(n):
    if len(n) == 2:
        ans = int(n[0])**5 + int(n[1])**5
        return ans if ans == int(n) else 0
 
    elif len(n) == 3:
        ans = int(n[0])**5 + int(n[1])**5 + int(n[2])**5
        return ans if ans == int(n) else 0
 
    elif len(n) == 4:
        ans = int(n[0])**5 + int(n[1])**5 + int(n[2])**5 + int(n[3])**5
        return ans if ans == int(n) else 0
    
    elif len(n) == 5:
        ans = int(n[0])**5 + int(n[1])**5 + int(n[2])**5 + int(n[3])**5 + int(n[4])**5
        return ans if ans == int(n) else 0

    elif len(n) == 6:
        ans = int(n[0])**5 + int(n[1])**5 + int(n[2])**5 + int(n[3])**5 + int(n[4])**5 + int(n[5])**5
        return ans if ans == int(n) else 0

    return 0



def main():
    total = 0
    for x in range(10, 10**7):
        total += fifthPower(str(x))

    print(total)

if __name__ == "__main__":
    main()
