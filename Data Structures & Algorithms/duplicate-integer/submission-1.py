class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                return True 
            else:
                count[num] = num
        return False

                

"""
so here what do is if we have seen a number add it to count with the key being the 
number and the value being the amount of times i have seen it
"""
