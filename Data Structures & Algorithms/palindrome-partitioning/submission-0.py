class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def check(st):
            left, right = 0, len(st) - 1
            palindrome = False
            while left <= right:
                if st[left] != st[right]:
                    return False
                else:
                    left += 1
                    right -= 1
                    palindrome = True
            return palindrome

        def dfs(i, path):
            if i >= len(s):
                res.append(path.copy())
                return

            # we have to make a decision, to take or not to take the next letter
            # path.append(s[i] + )
            # dfs(i + 1, path)
            # path.pop()
            # dfs(i + 1, path)

            for j in range(i, len(s)):
                if check(s[i:j+1]):
                    path.append(s[i : j + 1])
                    dfs(j + 1, path)
                    path.pop()

        dfs(0, [])
        return res
