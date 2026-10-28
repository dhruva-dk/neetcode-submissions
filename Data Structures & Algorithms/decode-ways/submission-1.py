# recurrence: 
# dp[0] = 1 if nums[0] != 0
# for 1...len(dp)
# if nums[i-1] != 0:
# dp[i] += dp[i-1]
# if nums[i-1] == 1 or == 2
# dp[i] += dp[i-2]

# trace: 
# 226
class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * len(s)

        if s[0] != '0':
            dp[0] += 1

        if len(s) == 1:
            return dp[-1]

        for i in range(1, len(s)):
            if int(s[i]) != 0:
                dp[i] += dp[i-1]

            if (s[i - 1] == '1') or (s[i - 1] == '2' and int(s[i]) <= 6):
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]

        return dp[-1]

        