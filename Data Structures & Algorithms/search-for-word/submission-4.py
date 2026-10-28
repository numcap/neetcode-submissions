class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        seen = set()

        ROWS = len(board)
        COLUMNS = len(board[0])

        def dfs(i, j, k):
            nonlocal res
            if k == len(word):
                res = True
                return
            if not (0 <= i < ROWS) or not (0 <= j < COLUMNS):
                return
            if board[i][j] != word[k]:
                return
            if (i, j) in seen:
                return


            seen.add((i, j))

            dfs(i + 1, j, k + 1)
            dfs(i - 1, j, k + 1)
            dfs(i, j + 1, k + 1)
            dfs(i, j - 1, k + 1)
            seen.remove((i,j))
            
        for i in range(ROWS):
            for j in range(COLUMNS):
                dfs(i, j, 0)
        return res
