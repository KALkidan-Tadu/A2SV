class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(set(coins))
        coins.sort(reverse = True)
        if amount == 0:
            return 0
        queue = deque()
        visited = set()
        for coin in coins:
            if amount - coin >= 0 and amount-coin not in visited:
                queue.append((amount- coin, 1))
                visited.add(amount-coin)

        while queue:
            remain, dist = queue.popleft()
            if remain == 0:
                return dist
            for coin in coins:
                if remain - coin >= 0 and remain-coin not in visited:
                    queue.append((remain- coin, dist + 1))
                    visited.add(remain-coin)
        
        return -1
                
