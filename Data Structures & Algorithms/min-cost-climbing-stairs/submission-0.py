# input: a list of costs per stairs
# output - a value represneting the minimum 
# cost to step from the 0th stair to n-th stair
# where n is the length of the array

# notes: you either jump the n+1th stair, or the n+2th stair
# can start on either the 0th or 1th floor


# let memo[i] = the minimum cost to get to stair i
# memo[0] = 0 (already there)
# memo[1] = 0 (already there)
# memo[i] = min(memo[i-1] + (cost[i - 1], memo[i-1] + cost[i-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]
        

        