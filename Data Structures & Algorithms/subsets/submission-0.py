class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current = []
        result = []


        def help(start):
            result.append(current.copy())
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                current.append(nums[i])
                help(i + 1)
                current.pop()

        help(0)
        return result

        