class Solution:
    # brute force
    # def maxProduct(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     out = - (1 << 32)
    #     if n == 1: return nums[0]
    #     for i in range(n):
    #         pr = 1
    #         maxPr = - (1 << 32)
    #         for j in range(i, n):
    #             pr *= nums[j]
    #             maxPr = max(pr, maxPr)
    #         out = max(out, maxPr)

    #     return out
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        minProd, maxProd = 1, 1 
        res = 0
        for i in range(n):
            if nums[i] == 0:
                minProd, maxProd = 1, 1
                continue
            nextMin = nums[i]*minProd
            nextMax = nums[i]*maxProd
            minProd = min(nextMin, nextMax, nums[i])
            maxProd = max(nextMin, nextMax, nums[i])
            res = max(res, maxProd)

        return res