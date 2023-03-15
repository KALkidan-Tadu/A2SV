class TopVotedCandidate:
    persons = []
    time = []
    d = defaultdict(int)
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.time = []
        self.d = defaultdict(int)
        maxVote = -1
        winner = -1
        for i in range(len(times)):
            self.d[persons[i]] += 1
            if self.d[persons[i]] >= maxVote:
                maxVote = self.d[persons[i]]
                winner = persons[i]
            self.time.append((times[i], winner))
                  
    def q(self, t: int) -> int:
        left, right = 0, len(self.time)-1

        while left <= right:
            mid = left + (right - left)//2

            if self.time[mid][0] == t:
                return self.time[mid][1]
            if self.time[mid][0] > t:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.time[right][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
