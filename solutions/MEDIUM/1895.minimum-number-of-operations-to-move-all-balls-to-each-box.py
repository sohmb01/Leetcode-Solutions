# Problem ID: 1895
# Title: Minimum Number of Operations to Move All Balls to Each Box
# Runtime: 7 ms

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        total = 0
        n = len(boxes)

        l,r = [0]*n,[0]*n
        cnt = 0
        for i in range(1,n):
            if boxes[i-1]=='1':
                cnt += 1
            l[i] = l[i-1]+cnt
        cnt = 0
        for i in range(n-2,-1,-1):
            if boxes[i+1] == '1':
                cnt+=1
            r[i] = r[i+1]+cnt
        ans = []
        for i in range(n):
            ans.append(l[i]+r[i])
        return ans
        
                