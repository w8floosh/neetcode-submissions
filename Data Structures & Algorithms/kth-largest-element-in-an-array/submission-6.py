class MinHeap:
    def __init__(self, nums: List[int]):
        self.heap = [None] + list(nums)
        self.build_heap()
    
    def sift_down(self, i: int):
        h = self.heap
        n = len(h)
        while (i << 1) < n:
            lci = i << 1
            rci = lci | 1
            smallest_child = rci if rci < n and h[lci] > h[rci] else lci
            if h[smallest_child] < h[i]:
                h[i], h[smallest_child] = h[smallest_child], h[i]
                i = smallest_child
            else: break

    def sift_up(self, i: int):
        h = self.heap
        while i > 1:
            parent = i >> 1
            if h[parent] <= h[i]: break
            h[parent], h[i] = h[i], h[parent]
            i = parent

    def build_heap(self):
        n = len(self.heap)
        curr = (n - 1) >> 1
        while curr > 0:
            self.sift_down(curr)
            curr -= 1

    def pop(self) -> int:
        h = self.heap
        root = h[1]
        last = h.pop()
        if len(h) > 1:
            h[1] = last
            self.sift_down(1)
        return root
    
    def kth_largest(self, k: int):
        while len(self.heap) - 1 > k:
            self.pop()
        return self.heap[1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int | None:
        heap = MinHeap(nums)
        return heap.kth_largest(k)