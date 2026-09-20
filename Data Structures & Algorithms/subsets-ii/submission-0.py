class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        output, current = [], []
        subdivide(nums, current, output, 0)
        return output

def subdivide(nums: List[int], current: List[int], subsets: List[List[int]], i: int):
    if not nums: return
    n = len(nums)
    if i >= n:
        subsets.append(current.copy())
        return

    current.append(nums[i])
    subdivide(nums, current, subsets, i+1)

    current.pop()
    
    while i+1 < n and nums[i] == nums[i+1]: i += 1
    subdivide(nums, current, subsets, i+1)

  