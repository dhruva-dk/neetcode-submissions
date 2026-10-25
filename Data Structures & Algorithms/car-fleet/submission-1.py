# (1, 3), (4, 2)
# (9, 3), (6, 2)

# (6, 2),

# (4, 2), (1, 2), (0, 1), (7, 1)
# 
# (7, 1), (1, 2), (0, 1)


# algorithm
# take tuples (distance remaining, speed)
# sort by distance remaining, inverse speed
# add the first car to the list of fleets
# for all remaining - if they will reach the destination before the
# first car, do not add, as they will sync before the end 
# otherwise, add to the fleet, list, they are the new slow bar
from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        def srt_cars(tup):
            a = tup[0]
            b = tup[1]
            return (a, -1 * b)

        for i in range(len(position)):
            pos = position[i]
            spd = speed[i]
            # how much left to go, speed
            cars.append((target - pos, spd ))

        cars.sort(key=srt_cars)


        fleets = []

        if len(cars) == 0:
            return 0

        fleets.append(cars[0])
        
        for i in range(1, len(cars)):
            cur_car = cars[i]

            # compare arrival times
            arrival_cur_car = cur_car[0] / cur_car[1]
            last = fleets[-1]
            arrival_last = last[0] / last[1]

            # only add to the fleet if this car is slow enought
            # that it won't meet the previous

            

            if arrival_cur_car > arrival_last:
                fleets.append(cur_car)

        return len(fleets)



        