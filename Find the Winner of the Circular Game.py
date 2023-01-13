class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for i in range(1, n+1):
            players.append(i)
        start = 0
        while(len(players) > 1):
            l = len(players)
            players.remove(players[(start+k-1)%len(players)])
            start = (start+k-1)%l

        return players[0]
