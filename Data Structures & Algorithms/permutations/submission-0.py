class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, arr, bool_arr):
            # when do i have a complete answer
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if bool_arr[i]:
                    continue
                path.append(nums[i])
                bool_arr[i] = True
                dfs(path, arr, bool_arr)
                path.pop()
                bool_arr[i] = False

        dfs([], [], [False] * len(nums))
        return res
