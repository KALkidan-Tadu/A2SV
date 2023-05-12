from typing import List
from collections import defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    visited = set()
        def dfs(node, parent):
            visited.add(node)
            
            for child in adj[node]:
                if child not in visited:
                    if dfs(child, node):
                        return True
                        
                elif child != parent:
                    return True
                    
            return False
		  
        for node in range(len(adj)):
            if node not in visited:
                if dfs(node, -1):
                    return 1
                    
        return 0
