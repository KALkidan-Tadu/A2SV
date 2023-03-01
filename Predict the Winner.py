class Solution:
    def optimize(self, nums, left, right):
        if left > right:
            return 0
        score1 = nums[left]+min(self.optimize(nums, left+1, right-1), self.optimize(nums, left+2, right))
        score2 = nums[right]+min(self.optimize(nums, left+1, right-1), self.optimize(nums, left, right-2))
        return max(score1, score2)

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        player1 = self.optimize(nums, 0, n-1)
        player2 = sum(nums[:n]) - player1

        if player1 >= player2:
            return True
        return False
