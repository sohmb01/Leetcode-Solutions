# Problem ID: 56
# Title: Merge Intervals
# Runtime: 17 ms

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def help(a,b):
            a= a+b
            print(a)
            return [min(a),max(a)]
        i,l = 1, len(intervals)
        j = 0
        ans= []
        
        intervals.sort(key = lambda x: x[0])
        ans.append(intervals[0])
        print(intervals)
        while i<l:
            if ans[j][1]>=intervals[i][0]:
                ans[j] = help(ans[j],intervals[i])
            else:
                ans.append(intervals[i])
                j+=1
            i+=1
        return ans
