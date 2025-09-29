# Problem ID: 135
# Title: Candy
# Runtime: 27 ms

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [0] * (n+2)
        ratings = [float("inf")] + ratings + [float("inf")]
        for i in range(1,n+1):
            if ratings[i]<=ratings[i-1] and ratings[i]<=ratings[i+1]:
                candies[i] = 1
        
        for i in range(1,n+1):
            if candies[i] == 1:
                j = i+1
                while j < n+2 and ratings[j]>ratings[j-1]:
                    candies[j] = candies[j-1]+1
                    j+=1
        
        for i in range(1,n+1):
            if candies[i] == 1:
                j = i-1
                while j >=0 and ratings[j]>ratings[j+1]:
                    candies[j] = max(candies[j+1]+1,candies[j])
                    j-=1
        
        return sum(candies) - (candies[0]+candies[-1])
