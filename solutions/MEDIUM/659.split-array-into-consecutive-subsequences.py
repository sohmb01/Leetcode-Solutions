# Problem ID: 659
# Title: Split Array into Consecutive Subsequences
# Runtime: 15 ms

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for num in nums:
            while heap and num > heap[0][0]+1:
                length = heappop(heap)
                if length[1] < 3:
                    return False
                
            if heap and num == heap[0][0]+1:
                length = heappop(heap)
                heappush(heap,(num, length[1]+1))
            else:
                heappush(heap,(num,1))
        while heap:
            if heappop(heap)[1] < 3:
                return False
        return True
            
            
            
