class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        chars = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        # print(chars)

        def dfs(i, comb):
            if len(digits) == len(comb):
                res.append(comb)
                return

            for c in digitToChar[digits[i]]:
                dfs(i+1, comb + c)


        dfs(0, "")
        return res
