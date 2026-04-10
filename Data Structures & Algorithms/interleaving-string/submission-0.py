class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        grid = [[False] * (m + 1) for _ in range(n + 1)]
        grid[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0 and grid[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    grid[i][j] = True
                if j > 0 and grid[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    grid[i][j] = True
        return grid[n][m]
