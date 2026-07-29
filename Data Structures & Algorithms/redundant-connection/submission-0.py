class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(n):    #we are defining find operation to check two nodes are already connecnted or not
           if parent[n] != n:
               parent[n] = find(parent[n])
           return parent[n]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:  #it means the nodes are already connected and they will form cycle
                return False
            parent[rootA] = rootB
            return True

        for a, b in edges:
            if not union(a, b):
                return[a, b]