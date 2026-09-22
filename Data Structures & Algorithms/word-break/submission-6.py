class Solution:
    # subproblem is: given the character at index i, does the substring before i have a valid segmentation?
    # to answer true or false at index i we must check if inserting a break in any position gives a valid segmentation.
    # if the prefix can't be broke in any split point, we can't have a valid segmentation
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if len(s) == 1 and s in wordDict:
            return True
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: 
                    dp[i] = True
                    break
        return dp[-1]