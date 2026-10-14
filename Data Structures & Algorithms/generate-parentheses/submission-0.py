class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, opened, closed):
            if n * 2 == len(path):
                res.append(path[:])
                return

            if opened < n:
                dfs(path + "(", opened + 1, closed)
            if closed < opened:
                dfs(path + ")", opened, closed + 1)
            # for p in ["(", ")"]:
            #     if p == "(":
            #         opened += 1
            #     else:
            #         opened -= 1
            #     path = path + p
            #     dfs(i + 1, path, opened)
            #     path = path[: len(path) - 1]

        dfs("", 0, 0)
        return res
