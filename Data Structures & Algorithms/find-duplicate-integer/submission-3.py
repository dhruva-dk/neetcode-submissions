# 4, 3, 2 ,2 , 1

# 4, 3, 2, 1, 

# 1 , 2 , 3 , 2 , 2

# 1, 3, 4, 2 ,2 

# loop 1
# slow = 3
# fast = nums[3] = 2
# loop 2
# slow = 2
# fast = 2

# cycle doesn't mean anything

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            print('\n')

            if slow == fast:
                break


        # find the cycle's start
        one = 0
        other = slow

        while True:
            one = nums[one]
            other = nums[other]

            if one == other:
                break

        return one

        



        