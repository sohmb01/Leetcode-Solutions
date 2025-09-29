# Problem ID: 447
# Title: Number of Boomerangs
# Runtime: 431 ms

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x1,y1 in points:
            distances = defaultdict(int)
            for x2,y2 in points:
                d = (x1-x2)**2 + (y1-y2)**2
                distances[d]+=1
            for cnt in distances.values():
                res += cnt*(cnt-1)
        return res