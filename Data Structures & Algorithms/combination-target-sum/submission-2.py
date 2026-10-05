class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start, total):
            # when target == path sum total is when we should append to res
            # we should return if the total is over target cause we missed
            if target <= total:
                if target == total: 
                    res.append(path[:])
                return
            
            # what choices can i make from here, well i can choose any num from nums
            for i in range(start, len(nums)):
                path.append(nums[i])
                total = sum(path)
                dfs(i, total)
                path.pop()
            
        dfs(0, 0)

        return res
