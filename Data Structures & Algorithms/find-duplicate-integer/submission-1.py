class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break # pointers meet because they both joined the loop

        slow = 0
        
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]

        return nums[slow]




