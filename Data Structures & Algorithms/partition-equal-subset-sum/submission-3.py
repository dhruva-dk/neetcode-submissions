class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # once you add the ith value, what are the possible sums:
        # that part optimizes an n! to an o(n) part


        # since we only use the previous i - 1th elem of the dp array, we can reuse our array
        # but we have to work backwards (not my own observation)

        # calculate sum
        dsum = 0
        for num in nums:
            dsum += num

        if dsum % 2 != 0:
            return False

        possible_subset_sum = [False] * (dsum + 1)
        possible_subset_sum[0] =  True

        for num in nums:
            # iterate backwards, we don't want to corrupt previous
            # sums which we're building on top of.
            for i in range(dsum, -1, -1):
                if i - num >= 0 and possible_subset_sum[i - num]:
                    possible_subset_sum[i] = True

        result = int(dsum/2)
        return possible_subset_sum[result]