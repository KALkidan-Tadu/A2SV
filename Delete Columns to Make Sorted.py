class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        
        for col in range(len(strs[0])):
            for row in range(len(strs)-1):
                if strs[row][col] > strs[row+1][col]:
                    deleted += 1
                    break

        return deleted
