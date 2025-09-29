# Problem ID: 134
# Title: Gas Station
# Runtime: 34 ms

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currgas = 0
        start = 0
        totalgas = 0
        for i in range(len(gas)):
            currgas = currgas + gas[i] - cost[i]
            totalgas = totalgas + gas[i] - cost[i]
            if currgas<0:
                currgas = 0
                start = i+1
        return start if totalgas>=0 else -1