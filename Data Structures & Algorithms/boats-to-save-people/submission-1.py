class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        contra_idx = len(people)
        i = 0

        while i < contra_idx:
            if people[contra_idx - 1] + people[i] <= limit:
                contra_idx -= 1

            boats += 1
            i += 1


        return boats
                

        