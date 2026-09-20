class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output, current = [], []
        combine(nums, current, 0, target, output, 0)
        return output

def combine(nums: List[int], current: List[int], currentSum: int, target: int, combinations: List[List[int]], i: int):
    if currentSum == target: 
        combinations.append(current.copy())
        return

    # j is used to avoid picking a number earlier than nums[i] in the next step of the path, 
    # so that unique combinations are not stored.
    # nums[i] can be used again after that step if not excluded again
    for j in range(i, len(nums)):
        if currentSum + nums[j] > target: continue
        current.append(nums[j])
        combine(nums, current, currentSum + nums[j], target, combinations, j)
        current.pop()