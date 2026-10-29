class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True 
            else:
                hashset.add(num)
        return False

                

"""
so here what do is if we have seen a number add it to count with the key being the 
number and the value being the amount of times i have seen it
"""
