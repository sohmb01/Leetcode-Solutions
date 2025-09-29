# Problem ID: 3647
# Title: Zero Array Transformation III
# Runtime: 204 ms

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        queries.sort(key = lambda x : x[0])
        heap = []
        delta = [0] * (len(nums)+1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += delta[i]
            while j<len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j+=1
            while operations<num and heap and -heap[0] >=i:
                operations+=1
                delta[-heappop(heap)+1] -= 1
            if operations < num:
                return -1
        return len(heap)