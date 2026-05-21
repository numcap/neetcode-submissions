class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        problem: we are given an array of prices we need to choose a single day to buy
        and a single day to sell to make the most profit, we can aslo make no
        transactions and return 0

        potential solution: we can easily run a double for loop to calculate every
        possible transaction and pick the most profitable one
        sliding window sounds like a 2 pointer approach we can still keep track of
        the most profitable transaction, but what we would do is take left pointer
        and check if it is greater than the right if it is we move the left, we then
        calculate the profit for buying and selling on these days, we then keep track
        of that profit with a max() then proceed by moving the right
        """

        maxProfit = 0

        l, r = 0, 0

        while l <= r:
            if l == r:
                r += 1
                continue
            elif r >= len(prices):
                break
            elif prices[l] > prices[r]:
                l += 1
                continue

            profit = prices[r] - prices[l]

            # maxProfit = max(maxProfit, profit)
            if maxProfit < profit:
                maxProfit = profit
            r += 1

        return maxProfit