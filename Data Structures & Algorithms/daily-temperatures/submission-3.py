class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        so i need to return an array of integers where the index is the day, and the value
        is the number of days until a tempurature is higher than the ith tempurature 

        potential solution: we can of course brute force this by iterating over it twice 
        but that would give us a O(n^2) solution
        lets see how we can use a stack in this situation, we can push the current day 
        onto the stack then check if that day is greater than the top of the stack
        we can then use the length to figure out 
        ---
        so the best solution is a monotonic stack (a stack that increases or decreases)
        we can do this by loading the index onto a stack, and when the top index's element
        (tempurature[stack[-1]]) is greater than the current element then pop the index
        off the stack and use that to make calculations, it will keep checking and keep 
        poping if the current element is greater than the index's element at
        the top of the stack
        """

        count = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                stack_ind = stack.pop()
                count[stack_ind] = i - stack_ind
        
            stack.append(i)

        return count