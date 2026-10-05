class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(candidates)

        def dfs(total, nums):
            if target <= total:
                if target == total:
                    res.append(path.copy())
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if target < nums[i] + total:
                    return
                path.append(nums[i])
                dfs(total + nums[i], nums[i+1:])
                path.pop()

        dfs(0, nums)
        return res
