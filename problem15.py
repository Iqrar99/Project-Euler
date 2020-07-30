"""
We can use Dynamic Programming to solve this problem.
The DP algorithm is:
    suppose r = row, and c = column
    if r = 0 or c = 0 then DP(r, c) = 1
    else DP(r, c) = DP(r-1, 1) +  DP(r, c-1)
"""


# we will use bottom-up approach
def DP(r, c):
    dp = [[0]*(r+1)]*(c+1)

    for i in range(r+1):
        for j in range(c+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[r][c]

def main():
    print(DP(20, 20))

if __name__ == "__main__":
    main()