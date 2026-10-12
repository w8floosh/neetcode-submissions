class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or int(s[0]) == 0: return 0
        if n == 1: return 1
        dp = [0] * (n+1) # kth cell gives the number of decoding ways of first k characters
        dp[0] = 1 # empty string can be decoded in just one way: no letters
        dp[1] = dp[0]
        for k in range(2, n+1):
            digit = int(s[k-1])
            if digit != 0: # single digit last letter is legal
                dp[k] += dp[k-1] # sum decoding ways of the first k-1 characters because the last character adds dp[k-1] new ways of decoding
            if 10 <= int(s[k-2:k]) <= 26: # double digit last letter is legal
                dp[k] += dp[k-2] # sum decoding ways of the first k-2 characters because the last character PAIR adds dp[k-2] new ways of decoding
            
        return dp[-1]
            