class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = set()

        def dfs(i, subset, picked):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for j in range(len(nums)):
                if not picked[j]:
                    subset.append(nums[j])
                    picked[j] = True
                    dfs(j, subset, picked)
                    subset.pop()
                    picked[j] = False

        dfs(0, [], [False] * len(nums))
        return res
