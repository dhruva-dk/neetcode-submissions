class Solution:
    def partition(self, s: str) -> List[List[str]]:

        curr = []
        result = []


        def isPal(string):
            start = 0
            end = len(string) - 1

            while (start < end):
                if string[start] != string[end]:
                    return False
                start+=1
                end-=1

            return True

        def help(remaining):
            if remaining == "":
                result.append(curr.copy())
                print(curr)
                return

            for end in range(1, len(remaining) + 1):
                candidate = remaining[:end]
                if isPal(candidate):
                    curr.append(candidate)
                    help(remaining[end:])
                    curr.pop()

            return


        help(s)
        return result



            
        