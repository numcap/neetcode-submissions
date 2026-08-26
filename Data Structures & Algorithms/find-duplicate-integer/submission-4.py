class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slowest = slow = fast = 0

        first = False

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        while True:
            slow = nums[slow]
            slowest = nums[slowest]
            if slow == slowest:
                return slow