from typing import List
def minFallingPathSum(matrix: List[List[int]]) -> int:
    N = len(matrix)
    dp = [[float("inf") for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[0][i] = matrix[0][i]
    for r in range(1, N):
        for c in range(N):
            mid = matrix[r-1][c]
            left = matrix[r-1][c-1] if c > 0 else float("inf")
            right = matrix[r-1][c+1] if c < N-1 else float("inf")
            # print(mid, left, right)
            matrix[r][c] = matrix[r][c] + min(mid, left, right)
    print(matrix)
    return min([matrix[N-1][i] for i in range(N)])    
    
# matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(minFallingPathSum(matrix))
