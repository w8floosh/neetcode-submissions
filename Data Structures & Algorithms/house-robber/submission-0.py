class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
    
        def dfs(i: int):
            if i >= len(nums):
                return 0
            
            if cache[i] >= 0: return cache[i]

            skip = dfs(i+1)
            rob = nums[i] + dfs(i+2)

            cache[i] = max(skip,rob)
            return cache[i]

        return dfs(0)


