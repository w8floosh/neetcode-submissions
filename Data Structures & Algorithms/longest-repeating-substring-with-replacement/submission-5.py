import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start, end = 0, 0
        freq = {}
        maxlen, maxfreq = 0, 0
        for i in range(n):
            end = i
            freq[s[i]] = freq.get(s[i], 0) + 1
            if freq[s[i]] > maxfreq:
                maxfreq = freq[s[i]]
            strlen = end+1 - start
            if strlen - maxfreq > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    freq.pop(s[start])
                start += 1
                maxlen = max(strlen-1, maxlen)
            else:                
                maxlen = max(strlen, maxlen)

        return maxlen


