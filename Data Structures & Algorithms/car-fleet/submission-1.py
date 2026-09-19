class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        velocities = zip(position, speed)
        sorted_velocities = bucketSort(list(velocities))
        fleet_times = []

        for pos, spd in sorted_velocities: 
            time = (target - pos) / spd
            if not fleet_times or fleet_times[-1] < time:
                fleet_times.append(time)

        return len(fleet_times)
            

def bucketSort(arr: List[tuple[int,int]]):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    positions = [p[0] for p in arr]
    nmax = max(positions)
    nmin = min(positions)
    for velocity in arr:
        bidx = 0 if nmax-nmin == 0 else int((velocity[0] - nmin)/(nmax-nmin)*(n-1))
        buckets[bidx].append(velocity)

    for b in buckets: b.sort(key=lambda p: p[0])

    sorted_arr = [item for bucket in buckets for item in bucket]
    sorted_arr.reverse()
    return sorted_arr
