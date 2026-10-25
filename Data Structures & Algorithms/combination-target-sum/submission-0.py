class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        result = []
        curr = []

        # appends all combinations with prefix of current curr
        # that add exactly <remaining> to curr to result
        def help(start, remaining):
            if remaining == 0:
                result.append(curr.copy())
                return
            elif remaining < 0:
                return


            for idx in range(start, len(nums)):
                curr.append(nums[idx])
                help(idx, remaining - nums[idx])
                curr.pop()


        help(0, target)
        return result
            
        