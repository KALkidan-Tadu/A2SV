class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = defaultdict(int)
        partition = []

        for index in range(len(s)-1, -1, -1):
            if s[index] not in lastindex:
                lastindex[s[index]] = index

        start = 0
        while start < len(s):
            end = lastindex[s[start]]
            index = start
            while index < end:
                if lastindex[s[index]] > lastindex[s[end]]:
                    end = lastindex[s[index]]
                index += 1
            partition.append(end-start+1)
            start = end+1

        return partition
