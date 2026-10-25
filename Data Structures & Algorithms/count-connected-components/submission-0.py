# strategy:
# create an adjacency list of n nodes
# iterate through each node
# if node not in seen
# increment total by 1
# dfs and add all to seen if not in seen

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        total = 0

        # construct the adjacency list
        nodes = {}
        for i in range(n):
            nodes[i] = []

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)


        def help(node):
            if node in seen:
                return

            seen.add(node)
            for child in nodes[node]:
                help(child)

        for node in range(n):
            if node not in seen:
                total +=1
                help(node)

        return total

        