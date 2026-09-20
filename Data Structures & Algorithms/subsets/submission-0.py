class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, current = [], []
        subdivide(nums, current, output, 0)
        return output

def subdivide(nums: List[int], current: List[int], subsets: List[List[int]], i: int):
    if not nums:
        return []
    if i >= len(nums):
        subsets.append(current.copy())
        return
    
    current.append(nums[i])
    subdivide(nums, current, subsets, i+1)

    current.pop()
    subdivide(nums, current, subsets, i+1)
