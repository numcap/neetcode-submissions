class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        so the question is asking, longest consecutive elements meaning longest amount of values that are 
        consective

        potential solution: immediately im thinking that we can sort the array which would be O(n) then iterate
        over and count the consecutive numbers, and recount every time it hits a number greater than i+1
        """

        nums = sorted(nums)
        n = len(nums)
        m = 1
        j = 1

        if n == 0:
            return 0

        for i in range(0, n-1):
            if (nums[i] + 1) == nums[i+1]:
                j += 1
                if j > m:
                    m = j
            elif nums[i] + 1 < nums[i+1]:
                j = 1
        
        return m