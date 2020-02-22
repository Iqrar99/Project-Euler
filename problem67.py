"""
This problem is similar with problem #18. We only need to save maximum calculation
in a cumulative sum list
"""


def main():
    with open('p067_triangle.txt', 'r') as infile:
        TRIANGLE = infile.read().strip().split('\n')
    
    for i in range(len(TRIANGLE)):
        TRIANGLE[i] = list(map(int, TRIANGLE[i].split(' ')))

    cumulative = [[0 for _ in range(len(TRIANGLE))]
                  for _ in range(len(TRIANGLE))]
    cumulative[0][0] = TRIANGLE[0][0]

    for r in range(1, len(TRIANGLE)):
        for c in range(r+1):
            if c == 0:
                cumulative[r][c] = cumulative[r-1][c] + TRIANGLE[r][c]
            elif c == r:
                cumulative[r][c] = cumulative[r-1][c-1] + TRIANGLE[r][c]
            else:
                cumulative[r][c] = max(
                    cumulative[r-1][c-1] +
                    TRIANGLE[r][c], cumulative[r-1][c] + TRIANGLE[r][c]
                )

    print(max(cumulative[len(TRIANGLE) - 1]))

if __name__ == "__main__":
    main()
