class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def dfs(start, total):
            # when target == path sum total is when we should append to res
            # we should return if the total is over target cause we missed
            if target <= total:
                if target == total: 
                    res.append(path[:])
                return
            
            # what choices can i make from here, well i can choose any num from nums
            # but if we already went through the first 3 nums then we can continue 
            # from that instead of doing them again, hence the start index
            for i in range(start, len(nums)):
                # if the total + the num we are on is greater than target then 
                # there is no point in continuing the DFS as we know that all
                # subsequent recursive calls will be greater since we sorted it
                # at the start
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                dfs(i, total + nums[i])
                path.pop()
            
        dfs(0, 0)

        return res
