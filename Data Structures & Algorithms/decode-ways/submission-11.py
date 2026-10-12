class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or int(s[0]) == 0: return 0
        if n == 1: return 1
        dp = [0] * n
        dp[0] = 1
        if int(s[1]) != 0:
            dp[1] += dp[0]
        if 10 <= int(s[:2]) <= 26:
            dp[1] += dp[0]
        for i in range(2, n):
            digit = int(s[i])
            if digit != 0: 
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
            if dp[i] + dp[i-1] == 0: 
                return 0
            
        return dp[-1]
            