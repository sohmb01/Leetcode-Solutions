# Problem ID: 1049
# Title: Minimum Domino Rotations For Equal Row
# Runtime: 50 ms

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        freq = [0] * 7
        for i in range(n):
            freq[tops[i]] += 1
            freq[bottoms[i]] += 1
        s = []
        for i in range(1,7):
            if freq[i] >= n:
                s.append(i)
        res = n+1
        print(s)
        for target in s:
            flag = True
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    flag = False
                    break
            if flag:
                cnt = max(tops.count(target),bottoms.count(target))
                res = min(min(cnt,n-cnt),res)
        
        return -1 if res == n+1 else res