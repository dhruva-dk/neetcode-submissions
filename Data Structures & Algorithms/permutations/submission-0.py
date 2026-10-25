class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        curr_set = set()

        def help():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in curr_set:
                    continue

                curr_set.add(nums[i])
                curr.append(nums[i])
                help()
                curr_set.remove(nums[i])
                curr.pop()


            
        help()
        return result
        