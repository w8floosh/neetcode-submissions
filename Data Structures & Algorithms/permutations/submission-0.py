class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output, current = [], []
        explore(nums, current, output, 0)
        return output

def explore(nums: List[int], current: List[int], permutations: List[List[int]], i: int):
    if len(current) >= len(nums):
        permutations.append(current.copy())
        return
        
    # try to put the current number in every position between numbers (first, between current[i] and current[i+1], last)
    for j in range(i+1): 
        explore(nums, current[:j] + [nums[i]] + current[j:], permutations, i+1)
        

    

    
    