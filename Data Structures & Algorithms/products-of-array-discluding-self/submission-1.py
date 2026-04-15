class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        return an array that has the product of the whole array execpt the one at the current index(i)

        potential solution: iterating over the array then we iterate again and get the product of all the values 
        in the array that are not on the variable of iteration.

        here we do a preffix suffix alogrithm
        """

        res = [1] * len(nums)
        
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]

        return res