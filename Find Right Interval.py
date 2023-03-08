class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ranges = defaultdict(int)
        answer = [-1]*len(intervals)

        for i in range(len(intervals)):
            ranges[intervals[i][0]] = i
        intervals.sort()

        for i in range(len(intervals)):
            left, right = i, len(intervals)-1
            while left <= right:
                mid = left + (right-left)//2
                if intervals[mid][0] >= intervals[i][1]:
                    answer[ranges[intervals[i][0]]] = ranges[intervals[mid][0]]
                    right = mid - 1
                else:
                    left = mid + 1  
        return answer
