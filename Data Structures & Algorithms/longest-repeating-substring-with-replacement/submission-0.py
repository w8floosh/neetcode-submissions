import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start, end = 0, 0
        freq = {chr(ord('A')+i): 0 for i in range(26)}
        maxlen = 0
        for i in range(n):
            end = i
            freq[s[i]] += 1
            maxfreq = max(freq.items(), key=lambda item: item[1])[1]
            strlen = len(s[start:end+1])
            if len(s[start:end+1]) - maxfreq > k:
                freq[s[start]] -= 1
                start += 1
                maxlen = max(strlen-1, maxlen)
            else:                
                maxlen = max(strlen, maxlen)

        return maxlen


