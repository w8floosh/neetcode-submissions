class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # use 2 pointers: start, curr, start points to current starting station and curr points to current attempted station.
        # at the first iteration, start=next=0 (start from station 0)
        # when attempting to travel to a station where gas count would go -k_curr (insufficient gas), accumulate -k_curr in gasRequired (starting from 0), move start and curr to the attempted station as new starting point. This means that we can go from station 0 to station curr only if the remaining gas after traveling the rest of the path is > k.
        # proceed until reaching station 0 again. If no attempts fail and gasRequired <= gasRemaining, then start is the solution
        n = len(gas)
        if n == 1: return 0 if gas[0] >= cost[0] else -1
        gasRequired, gasRemaining = 0, 0 # start with empty tank
        start, nextStation = 0, 1
        while nextStation%n != 0:
            gasRemaining += gas[nextStation-1]
            gasAfterTravel = gasRemaining - cost[nextStation-1]
            if gasAfterTravel < 0:
                gasRequired += -gasAfterTravel
                gasRemaining = 0
                start = nextStation
                nextStation = start+1
            else:
                gasRemaining = gasAfterTravel
                nextStation = nextStation+1
        
        gasRemaining += gas[nextStation-1]
        gasAfterTravel = gasRemaining - cost[nextStation-1]
        if gasAfterTravel < 0:
            gasRequired += -gasAfterTravel
            gasRemaining = 0
            start = nextStation
            nextStation = start+1
        else:
            gasRemaining = gasAfterTravel
            nextStation = nextStation+1
        
        return start if gasRemaining >= gasRequired else -1

            

