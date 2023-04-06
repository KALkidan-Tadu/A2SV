class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set()
        ans = []

        for edge in edges:
            nodes.add(edge[1])
        
        for i in range(n):
            if i not in nodes:
                ans.append(i)
        
        return ans
