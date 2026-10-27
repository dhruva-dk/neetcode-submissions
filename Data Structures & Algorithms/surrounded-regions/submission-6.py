# strategy
# hard to find the edge O for an entire region

# work outwards from edge os
# mark as seen
# then for 


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [(1,0), (0,1), (-1,0), (0, -1)]

        def mark_edge(r, c):
            if r < 0 or r >= len(board):
                return
            if c < 0 or c >= len(board[0]):
                return
            if board[r][c] == 'S' or board[r][c] == 'X':
                return

            board[r][c] = 'S'

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                mark_edge(nr, nc)

        for i in range(len(board)):
            mark_edge(i, 0)
            mark_edge(i, len(board[0]) - 1)
        for i in range(len(board[0])):
            mark_edge(0, i)
            mark_edge(len(board) - 1, i)

        #print(board)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'


            
