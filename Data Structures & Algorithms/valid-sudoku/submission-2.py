class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrid = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                if n in rows[r]:
                    return False
                if n in cols[c]:
                    return False
                if n in subgrid[r // 3][c // 3]:
                    return False
                rows[r].add(n)
                cols[c].add(n)
                subgrid[r // 3][c // 3].add(n)
        return True