class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        question: we need to search for the smallest number/element in the array

        potential solution: we can perform a binary search to find the point at
        which the array flips, we can try to do this by keeping track of the
        previous mid point to compare to see if its greater than or less than
        the current mid point, to see if we are near the point at which the
        array flips
        """

        l, r = 0, len(nums) - 1
        # prev_mid = 0

        if nums[l] < nums[r]:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < nums[l]:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                elif nums[mid+1] < nums[mid]:
                    return nums[mid + 1]
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                elif nums[mid+1] < nums[mid]:
                    return nums[mid + 1]
                else:
                    l = mid + 1
            else:
                return nums[mid]