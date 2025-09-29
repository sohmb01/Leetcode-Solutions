# Problem ID: 883
# Title: Car Fleet
# Runtime: 143 ms

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(p,s) for p, s in zip(position,speed)]
        times.sort(key = lambda x:x[0], reverse = True)
        
        stack = []
        for p,s in times:
            time = (target - p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)



