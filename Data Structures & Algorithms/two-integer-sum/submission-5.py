class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} #value -> index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index

        """
        so what i am thinking is we can create a hashmap that as we go through stores
        the value and index of each element, then when it passes the the previous 
        elements we can check in the previous elmenent if it is there and when we 
        return the value its [prevdict, index]
        """