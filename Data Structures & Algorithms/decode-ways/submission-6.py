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
            if digit != 0:
                dp[k] += dp[k-1]
            if 10 <= int(s[k-2:k]) <= 26:
                dp[k] += dp[k-2]
            

        return dp[-1]
            