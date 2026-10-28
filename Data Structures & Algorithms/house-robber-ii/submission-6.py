

# [2, 9, 10, ]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def help(arr):
            rob = [0] * len(arr)
            rob[0] = arr[0]
            if len(rob) == 1:
                return rob[0]
            rob[1] = max(arr[1], rob[0])
            for i in range(2, len(rob)):
                rob[i] = max(rob[i-2] + arr[i], rob[i-1])

            return rob[-1]

        return max(help(nums[0:len(nums)-1]), help(nums[1:len(nums)]))




                

        

        