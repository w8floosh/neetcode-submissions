import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = [(distance([0,0], point), point) for point in points]
        heapq.heapify(pairs)
        output = []
        while points and k > 0:
            output.append(heapq.heappop(pairs)[1])
            k -= 1

        return output
    
def distance(a: List[int], b: List[int]) -> float:
    if len(a) != 2 or len(b) != 2: return -1
    return math.dist(a,b)