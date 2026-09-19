class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        velocities = zip(position, speed)
        sorted_velocities = sorted(velocities, reverse=True)
        fleet_times = []

        for pos, spd in sorted_velocities: 
            time = (target - pos) / spd
            if not fleet_times or fleet_times[-1] < time:
                fleet_times.append(time)

        return len(fleet_times)
