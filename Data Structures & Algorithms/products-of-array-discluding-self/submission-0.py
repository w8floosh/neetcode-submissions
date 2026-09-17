class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # length of prefix product array
        pL = [1] * n
        pR = [1] * n
        output = [-1] * n
        for i in range(n-1):
            pL[i+1] = pL[i] * nums[i]
            pR[i+1] = pR[i] * nums[n-1-i]

        for i in range(n):
            output[i] = pL[i] * pR[n-1-i] # -1 because we exclude the ith element
        
        return output

# [1,2,4,6]

# i = 1 [1,1,1,1] [1,6,1,1]
# i = 2 [1,1,2,1] [1,6,24,1]
# i = 3 [1,1,2,4] [1,6,24,]



