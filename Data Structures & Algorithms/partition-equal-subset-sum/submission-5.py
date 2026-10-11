class Solution:
    # bruteforce: 
    # for each subset of size 0 < k < n, compare its sum with the complementary of it 
    # when len(subset) + len(complementary) = len(nums).
    # We make a tree where we store 2 arrays (the 2 subsets). At root both arrays are empty
    # We start from element 0 and we recursively choose either to add the ith element to the first subset or to the second
    # def canPartition(self, nums: List[int]) -> bool:
    #     if sum(nums) % 2 == 1: return False

    #     def equalSumPartition(i: int, subset1: List[int], subset2: List[int]) -> bool:
    #         if len(subset1) + len(subset2) == len(nums):
    #             return sum(subset1) == sum(subset2)
            
    #         subset1.append(nums[i])
    #         out = equalSumPartition(i+1, subset1, subset2)
    #         subset1.pop(-1)
    #         if out: return True
    #         subset2.append(nums[i])
    #         out = equalSumPartition(i+1, subset1, subset2)
    #         subset2.pop(-1)
    #         return out

    #     return equalSumPartition(0, [], [])

    # dp solution:
    # 
    def canPartition(self, nums: List[int]) -> bool:
        summa = sum(nums)
        if summa % 2 == 1: return False
        hs = summa >> 1
        dp = [False] * (hs+1)
        dp[0] = True
        for n in nums:
            nextDp = dp.copy()
            for s in range(n, hs+1):
                nextDp[s] = dp[s] or dp[s - n]
            del dp
            dp = nextDp
        return dp[-1]
    
