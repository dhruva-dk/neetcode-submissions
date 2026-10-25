class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []


        # recursive contract: includes all unique combinations of candidates, beginning with this prefix, inclusive by choosing a starting point for next elem



        nums = sorted(candidates)
        print


        def help(start, remaining):
            if remaining == 0:
                result.append(curr.copy())
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                help(i + 1, remaining - nums[i])
                curr.pop()

        help(0, target)
        return result


