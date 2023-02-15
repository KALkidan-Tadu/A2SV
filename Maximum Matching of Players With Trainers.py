class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p, t = 0, 0
        counter = 0

        while p<len(players) and t<len(trainers):
            while t<len(trainers) and trainers[t] < players[p]:
                t += 1
            if t<len(trainers):
                counter += 1
                t += 1
                p += 1
        
        return counter
