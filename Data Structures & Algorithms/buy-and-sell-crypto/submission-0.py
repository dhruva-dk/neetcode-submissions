class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        most_profit = 0

        for day in range(len(prices)):
            most_profit = max(most_profit, prices[day] - lowest)
            lowest = min(lowest, prices[day])

        return most_profit