# Problem ID: 621
# Title: Task Scheduler
# Runtime: 21 ms

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for task in tasks:
            idx = ord(task)-ord('A')
            freq[idx] +=1
        freq.sort()

        maxFreq = freq[25]-1
        idle = maxFreq * n

        for i in range(24,-1,-1):
            idle -= min(maxFreq,freq[i])
        return idle+len(tasks) if idle>0 else len(tasks)
