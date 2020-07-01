"""
This problem can be done using Dynamic Programming: Coin Change combinations.
The complexity will be O(mn).
"""

def coin_change(s:list, n:int) -> int:
    """
    function to get total combinations to get n value based
    on the coin list.
    """
    
    m = len(s)
    dp_table = [[0 for _ in range(m)] for _ in range(n + 1)]

    for col in range(m):
        dp_table[0][col] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = dp_table[i - s[j]][j] if i - s[j] >= 0 else 0
            y = dp_table[i][j - 1] if j >= 1 else 0

            dp_table[i][j] = x + y

    return dp_table[n][m - 1]

def main():
    target = 200
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

    answer = coin_change(coin_list, target)

    print(f"answer : {answer} ways")

if __name__ == "__main__":
    main()