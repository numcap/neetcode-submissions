class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        seen = set()

        def dfs(i, j, k):
            nonlocal res
            if (not (0 <= i < len(board[0])) or not (0 <= j < len(board))) or board[j][i] != word[k]:
                return
            if (j, i) not in seen:
                seen.add((j,i))
            else:
                return
            if len(word) - 1 == k:
                res = True
                return
            print("i", i)
            print("j", j)
            print("k", k)
            print("\n")
            dfs(i + 1, j, k + 1)
            dfs(i, j + 1, k + 1)
            dfs(i - 1, j, k + 1)
            dfs(i, j - 1, k + 1)
            seen.remove((j,i))

        for i in range(len(board[0])):
            for j in range(len(board)):
                dfs(i, j, 0)
        return res
