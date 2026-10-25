class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        curr = []
        result = []

        nums.sort()
  


        # recursive contract: given a curr prefix, return all possible non duplicate subsets beginning with the current prefix
        def help(start):
            result.append(curr.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                help(i + 1)
                curr.pop()

        help(0)
        return result



        