class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        problem: we need to find a index of the value given after the sorted array
        is rotated

        potential solution: we could perform a binary search on the rotated array
        and compare the mid to the left or right pointer to see where the value is
        since it is sorted, then keep performing the search
        """

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        arrs = [nums[0:l], nums[l : len(nums)]]
        print(arrs)

        for index, arr in enumerate(arrs):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return mid if index == 0 else mid + len(arrs[0])
        return -1