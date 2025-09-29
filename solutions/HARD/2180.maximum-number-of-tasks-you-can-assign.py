# Problem ID: 2180
# Title: Maximum Number of Tasks You Can Assign
# Runtime: 1824 ms

from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def check(mid):
            t = SortedList(tasks[:mid])
            w = workers[-mid:]
            p = pills

            for worker in w:
                task = t[0]
                if worker >= task:
                    t.pop(0)
                elif worker + strength >= task and p:
                    taskId = t.bisect_right(worker+strength)
                    t.pop(taskId-1)
                    p-=1
                else:
                    return False
            return True
        
        
        
        l,r = 0,min(len(tasks),len(workers))
        while l<r:
            mid = (l+r+1)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l