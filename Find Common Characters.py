class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dictionary = []
        repeated = []
        for word in words:
            dictionary.append(Counter(word))

        for value in dictionary[0]:
            minfreq = dictionary[0][value]
            for index in range(1, len(dictionary)):
                if value not in dictionary[index]:
                    minfreq = 0
                    break
                minfreq = min(minfreq, dictionary[index][value])
            for i in range(minfreq):
                repeated.append(value)
        return repeated
                    
