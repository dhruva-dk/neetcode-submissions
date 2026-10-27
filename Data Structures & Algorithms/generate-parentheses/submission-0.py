# all possible combinations: 
# recursive backtracking

# base case: 
# open = 0 and closed = 0
# append current string to list
# if open > 0 and closed > 0
# try open - 1 with adding (
# try closed - 1 with adding ) only if string[-1] is open

# if open 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def valid(curr):
            st = []
            for c in curr:
                if c == '(':
                    st.append(c)

                else:
                    if not st:
                        return False
                    st.pop()

            return len(st) == 0

        def recurse(open_ct, closed_ct, curr):
            if open_ct == 0 and closed_ct == 0 and valid(curr): 
                results.append(curr)
                return

            # at least 1 has remaining
            if open_ct > 0:
                recurse(open_ct - 1, closed_ct, curr + '(')

            if closed_ct > 0:
                recurse(open_ct, closed_ct - 1, curr + ')')

            # don't need t oclean up curr as its immutable, will
            # be copied 

        recurse(n, n, "")
        return results
        