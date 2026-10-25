class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1map = defaultdict(int)

        for c in s1:
            s1map[c]+=1


        s2map = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            s2map[s2[right]] += 1
            
            while right - left + 1 > len(s1):
                s2map[s2[left]] -= 1
                left += 1


            if (right - left + 1 == len(s1)):
                # we have the window map, now check
                holds = True

                for c in s2map:
                    if s2map[c] != s1map[c]:
                        holds = False
                        break

                if holds:
                    return True

        return False

        


            


        
        