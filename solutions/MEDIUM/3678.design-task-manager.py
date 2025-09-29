# Problem ID: 3678
# Title: Design Task Manager
# Runtime: 398 ms

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task = {task : (user, priority) for user, task, priority in tasks}
        self.heap = [(-priority, -task) for _, task, priority in tasks]
        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (userId, priority)
        heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task[taskId] = (self.task[taskId][0], newPriority)
        heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.task[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heappop(self.heap)
            if -taskId in self.task and self.task[-taskId][1] == -priority:
                user = self.task[-taskId][0]
                del self.task[-taskId]
                return user
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()