class Solution:
    # with memoization
    # def rob(self, nums: List[int]) -> int:
    #     cache = [-1] * len(nums)
    
    #     def dfs(i: int):
    #         if i >= len(nums):
    #             return 0
            
    #         if cache[i] >= 0: return cache[i]

    #         skip = dfs(i+1)
    #         rob = nums[i] + dfs(i+2)

    #         cache[i] = max(skip,rob)
    #         return cache[i]

    #     return dfs(0)

    # with tabulation
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return -1
        if n == 1: return nums[0]
        dp = [-1] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]


