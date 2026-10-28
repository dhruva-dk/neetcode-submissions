

# [2, 9, 10, ]
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        dptot = 0

        if len(nums) == 1:
            return nums[0]


        for count in range(3):
            ournums = None
            if count == 0:
                ournums = nums[0:len(nums) - 1]
            if count == 1:
                ournums = nums[1:len(nums)]
            if count == 2:
                ournums = nums[1:len(nums) - 1]

            
            rob = [0] * len(ournums)
            if len(ournums) == 0:
                continue

            print(ournums)


            rob[0] = ournums[0]

            if len(rob) == 1:
                dptot = max(dptot, ournums[0])
                continue

            rob[1] = max(rob[0], ournums[1])

            for i in range(2, len(rob)):
                rob[i] = max(rob[i-2] + ournums[i], rob[i-1])

            print(rob)
            dptot = max(dptot, rob[-1])

        return dptot


                

        

        