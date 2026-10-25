from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        result = []
        
        # graph represents dependencies flowing outwards
        prerequisite_of = defaultdict(list)

        # inwards flowing dependency count
        needs_prerequisite = [0] * numCourses


        for postreq, prereq in prerequisites:
            prerequisite_of[prereq].append(postreq)
            needs_prerequisite[postreq] += 1


        # now we peel back the onion. for every course which has no prereq (needs_prerequisite is empty)
        # we "take it" and remove it from that corresponding needs_prerequisite entry


        q = deque()

        for course in range(numCourses):
            if needs_prerequisite[course] == 0:
                q.append(course)


        while q:
            took_course = q.popleft()
            result.append(took_course)

            for postreq in prerequisite_of[took_course]:
                needs_prerequisite[postreq] -= 1
                if needs_prerequisite[postreq] == 0:
                    q.append(postreq)


        if len(result) == numCourses:
            return result

        return []




        
        