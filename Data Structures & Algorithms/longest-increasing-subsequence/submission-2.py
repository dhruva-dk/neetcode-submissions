class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        maxdp = 1
        for i in range(1, len(nums)):
            mindp = 0
            partofsubseq = False
            for j in range(i):
                if nums[j] < nums[i]:
                    partofsubseq = True
                    mindp = max(dp[j], mindp)

            dp[i] = mindp + 1
            maxdp = max(dp[i], maxdp)

        return maxdp





# store longest seen so far
# store