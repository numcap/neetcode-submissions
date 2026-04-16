class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        problem: we want to search for a target in an array of numbers and
        return the index of the value in nums

        potential solution: here we can perform a binary search, where what
        we would do is divide nums by 2 and seeing if the value is greater,
        less than or equal to the number then discard the other section
        based off the results
        """

        track = -1

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2

            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        
        return -1
