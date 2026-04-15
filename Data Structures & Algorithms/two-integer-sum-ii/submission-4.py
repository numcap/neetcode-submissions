class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        we need to return an array of 2 indices that add up to the target, 
        index1 < index2 
        
        potential solution: sliding window approach, where we can have the R pointer 
        go up until the it reaches just before the target, then the L pointer 
        can follow suit, we then check the addition of each pointer
        """
        L = 0
        R = len(numbers) - 1

        while L < R:
            curr_sum = numbers[L] + numbers[R]

            if curr_sum == target:
                return [L+1, R+1]

            if curr_sum < target:
                L+=1
            else:
                R-=1