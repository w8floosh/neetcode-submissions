class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1
        
        # create n+1 buckets where index = freq
        buckets = [[] for _ in range(n+1)]

        # place each element in its frequency bucket
        for num, f in freq.items():
             buckets[f].append(num)
            
        output = []
        for i in range(n+1):
            output.extend(bn for bn in [num for num in buckets[n-i]])
            k = k - len(buckets[n-i])
            if k <= 0: return output
        
        return output

