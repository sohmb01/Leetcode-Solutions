# Problem ID: 146
# Title: LRU Cache
# Runtime: 114 ms

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        ret = -1
        if key in self.lru:
            ret = self.lru[key]
            self.lru.pop(key)
            self.lru[key] = ret
        return ret

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru:
            self.lru.pop(key)
        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last = False)
      
