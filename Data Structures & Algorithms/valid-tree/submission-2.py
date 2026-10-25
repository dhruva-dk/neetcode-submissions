# input is an edge list of number of nodes, then edges between nodes
# output: boolean representing whether the graph is acyclic

# strategy:
# dfs function: (curr, parent) - returns whether that child has seen a node other than its parent
# seen set
# start at node 0 
# go through children
# if a child is seen and not your parent: 
# return false
# otherwise, return true

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # convert edge list into an adj list
        items = {}
        seen = set()

        for i in range(n):
            items[i] = []
        for n1, n2 in edges:
            items[n1].append(n2)
            items[n2].append(n1)

        def help(curr, parent):
            # go through your children
            # if they are seen and not yoru parent, return false.

            for child in items[curr]:
                if child in seen and child != parent:
                    return False
                if child in seen: 
                    continue
                
                seen.add(child)
                if not help(child, curr):
                    return False

            return True

        acyclic = True
        seen.add(0)
        for child in items[0]:
            seen.add(child)
            if not help(child, 0):
                return False

        return len(seen) == n
            

        