class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        return an array that has the product of the whole array execpt the one at the current index(i)

        potential solution: iterating over the array then we iterate again and get the product of all the values 
        in the array that are not on the variable of iteration 
        """

        output = [1] * len(nums)

        for i in range(len(nums)):

            for index, num in enumerate(nums):
                if i == index: continue
                output[i] *= num
                
        return output