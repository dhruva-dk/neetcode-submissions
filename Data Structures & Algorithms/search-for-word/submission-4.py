class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # return true if the word may be found with the current valid prefix and down/right motion


        prefix = []
        path = set()

        def help(i, j):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            if (i, j) in path:
                return False
            elif "".join(prefix) == word:
                return True
            elif len(prefix) >= len(word):
                return False
            
            prefix.append(board[i][j])
            path.add((i, j))

            if "".join(prefix) == word:
                return True

            result =  help(i + 1, j) or help(i, j+1) or help(i - 1, j) or help(i, j - 1)
            prefix.pop()
            path.remove((i, j))
            return result


        for i in range(len(board)):
            for j in range(len(board[0])):
                if help(i, j):
                    return True

        return False
         
