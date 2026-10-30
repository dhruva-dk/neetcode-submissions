# start out with brute force
# from each element - multiply, check if greater than max
# until end
# what can we store to make this faster? 
# store the minimum and the maximum at each point

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxes = [0] * len(nums)
        mins = [0] * len(nums)


        maxes[0] = nums[0]
        mins[0] = nums[0]

        for i in range(1, len(nums)):
            maxes[i] = max(maxes[i-1] * nums[i], nums[i], mins[i-1] * nums[i])
            mins[i] = min(mins[i-1] * nums[i], nums[i], maxes[i-1] * nums[i])

        return max(maxes)
