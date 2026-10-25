# input - a grid of numbers representing water or land
# output - the maximum area of contiguous 1s, top down, left right, no diagonals

# tracing - look for first 1
# do dfs(curr sum):
# if a 0, return curr sum
# if 1, set to 0, dfs neighbors with (curr sum + 1)
# set the rolling max to result of dfs
# look for next 1
# total time complexity: o(n^2), traverse the whole grid, hit a node at most 5 times

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c, amt):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return amt
            if grid[r][c] == 0:
                return amt


            # not seen yet
            # set to seen
            grid[r][c] = 0
            amt += 1
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in dirs:
                amt = max(amt, dfs(r + dr, c + dc, amt))

            return amt


        roll_max = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    roll_max = max(roll_max, dfs(r, c, 0))

        return roll_max
        