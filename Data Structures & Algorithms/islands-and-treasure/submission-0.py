# input: a grid of cells: -1 is untraversable water, 0 is treasure, INF is land
# output - mutate the grid so that cells > 0 have their distance to treasure cells

# strategy
# shortest path - bfs outwards until there are no more land cells to enqueue
# add all treasure indices to initial queue
# set level = 1
# iterate through all emlements in the queue, if they are land cells, add their neighbor and set their
# value to level
# increment level
# repeat until queue empty

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # iterate through the grid and find treasures
        q = deque()
        seen = set()

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))

        # now bfs while queue isn't empty
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        level = 1
        while len(q) > 0:
      
            for _ in range(len(q)):
                # process this level
                popped = q.popleft()
                r = popped[0]
                c = popped[1]

                seen.add((r, c))

                # if this is not a treasure (never water as we don't add water to queue)
                # set its distance to the level
            
                
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        # invalid oob, don't add to queue
                        continue

                    elif grid[nr][nc] == -1:
                        # water, can't traverse
                        continue

                    # land or treasure
                    if grid[nr][nc] == 2147483647: 
                        q.append((nr,nc))
                        # mark as seen and add level
                        grid[nr][nc] = level

            level += 1

                



                



        