class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(i, summ):
            if summ == target:
                res.append(path.copy())
                return
            if summ > target:
                return

            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j, summ + nums[j])
                path.pop()

        
        dfs(0,0)
        return res
