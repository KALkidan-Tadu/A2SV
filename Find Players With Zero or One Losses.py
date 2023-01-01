class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        oneLoss = []
        noLoss = []
        losers = {}
        players = set()
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            if match[1] in losers:
                losers[match[1]] += 1
            else:
                losers[match[1]] = 1
        players = list(players)
        for player in players:
            if player not in losers:
                noLoss.append(player)
            elif losers[player] == 1:
                oneLoss.append(player)
        return [sorted(noLoss), sorted(oneLoss)]


        
