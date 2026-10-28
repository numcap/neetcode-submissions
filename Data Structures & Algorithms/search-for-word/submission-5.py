class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        seen = set()

        ROWS = len(board)
        COLUMNS = len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if not (0 <= i < ROWS) or not (0 <= j < COLUMNS):
                return False
            if board[i][j] != word[k]:
                return False
            if (i, j) in seen:
                return False

            seen.add((i, j))

            res = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            seen.remove((i, j))
            return res

        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i, j, 0):
                    res = True
        return res
