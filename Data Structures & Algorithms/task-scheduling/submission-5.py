import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap = dict([(chr(ord("A")+i), 0) for i in range(26)])

        # for task in tasks:
        #     hashmap[task] += 1

        # mainq = list(filter(lambda x: x[0] > 0, [(freq, task) for task, freq in hashmap.items()]))
        # pendingq = deque()
        
        # heapq.heapify_max(mainq)

        # cycles = 0

        # while mainq or pendingq: 
        #     cycles += 1
        #     executed = None
        #     if pendingq and pendingq[0][0] == 0:
        #         wait, freq, task = pendingq.popleft()
        #         heapq.heappush_max(mainq, (freq, task))

        #     if mainq:
        #         freq, task = heapq.heappop_max(mainq)
        #         executed = task
        #         if freq > 1: # start first execution and move identical executions to a queue, restoring one after n cycles
        #             pendingq.append((-n, freq-1, task))

        #     for i in range(len(pendingq)):
        #         wait, freq, task = pendingq[i]
        #         if executed == task: continue
        #         pendingq[i] = (wait+1, freq, task)

        # return cycles
        counts = list(Counter(tasks).values())
        max_freq = max(counts)
        num_max = counts.count(max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)