class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parens = '([{'
        cto = {}
        cto[')'] = '('
        cto['}'] = "{"
        cto[']'] = '['

        for c in s:
            # if open paren, add to stack
            if c in open_parens:
                stack.append(c)

            else:
                # find corresponding open
                correspond = cto[c]

                # check if stack matches

                if not stack or stack[-1] != correspond:
                    return False


                stack.pop()

        return len(stack) == 0
        