import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start, end = 0, 0
        freq = {}
        maxlen = 0
        for i in range(n):
            if not freq.get(s[i]):
                freq[s[i]] = 0
            end = i
            freq[s[i]] += 1
            maxfreq = max(freq.items(), key=lambda item: item[1])[1]
            strlen = len(s[start:end+1])
            if len(s[start:end+1]) - maxfreq > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    freq.pop(s[start])
                start += 1
                maxlen = max(strlen-1, maxlen)
            else:                
                maxlen = max(strlen, maxlen)

        return maxlen


