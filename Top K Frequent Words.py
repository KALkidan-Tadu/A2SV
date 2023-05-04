class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        heap = []
        answer = []
        for word in words:
            count[word] += 1
        for key in count.keys():
            heappush(heap, (-1 * count[key], key))

        while heap:
            c, word = heappop(heap)
            answer.append(word)

        return answer[:k]
