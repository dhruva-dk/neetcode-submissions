class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for edge in edges:
            # try to find v
            st = [edge[0]]
            seen = set()
            while st:
                popped = st.pop()
                if popped in seen:
                    continue
                seen.add(popped)
                if popped == edge[1]:
                    return edge

                for adjacent in adj[popped]:
                    st.append(adjacent)


            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


            

        return ["WTF"]
            

            
        