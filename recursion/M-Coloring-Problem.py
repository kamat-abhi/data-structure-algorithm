"""
Approach(Backtracking)
1. Represent the graph as an adjacency list
2. Try to assign colors to each vertex (from 1 tp m)
3. Before coloring a vertex. check if assigning the chosen color is safe
4. If we can assign colors to all vertices, return True
otherwise, if no coloring is possible, return False

"""
class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        def isSafe(node, color, adj, c):
            for neigh in adj[node]:
                if color[neigh] == c:
                    return False
            return True
            
        def solve(node, color, adj, m, v):
            if node == v:
                return True
            for c in range(1, m+1):
                if isSafe(node, color, adj, c):
                    color[node] = c
                    if solve(node+1, color, adj, m, v):
                        return True
                    color[node] = 0
                    
            return False
            
        adj = [[] for _ in range(v)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        color = [0] * v
        return solve(0, color, adj, m, v)