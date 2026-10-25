class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        parents = [i for i in range(len(edges) + 1)]
        print(parents)

        def find(i):
            seen = []
            while parents[i] != i:
                i = parents[i]
                seen.append(i)
            for j in seen:
                parents[j] = i
            return i

        def connect(i, j):
            if find(i) == find(j):
                return False
            parents[find(j)] = find(i)
            return True

        for edge in edges:
            if not connect(edge[0], edge[1]):
                return edge
            

        return ["WTF"]
            

            
        