# start out with brute force
# from each element - multiply, check if greater than max
# until end
# what can we store to make this faster? 
# store the minimum and the maximum at each point

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # only storing 0 in dp - can get away with 1 variable
        cur_max = nums[0]
        cur_min = nums[0]
        # use tuple assigne when updating your max and min to avoid temp vars

        best = cur_max
        for i in range(1, len(nums)):

            cur_max, cur_min = max(cur_max * nums[i], nums[i], cur_min * nums[i]), min(cur_max * nums[i], nums[i], cur_min * nums[i])

            best = max(best, cur_max, cur_min)


        return best
