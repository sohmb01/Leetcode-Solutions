# Problem ID: 1819
# Title: Construct the Lexicographically Largest Valid Sequence
# Runtime: 7 ms

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(l,i,vi):
            if i >= k:
                return True
            if l[i]:
                return backtrack(l,i+1,vi)
            for num in reversed(range(1,n+1)):
                if num == 1 and not vi[num]:
                    l[i] = num
                    vi[num] = True
                    if backtrack(l,i+1,vi):
                        return True
                    l[i] = 0
                    vi[num] = False
                else:
                    if i+num < k and not vi[num] and not l[i] and not l[i+num]:
                        l[i],l[i+num] = num,num
                        vi[num] = True
                        if backtrack(l,i+1,vi):
                            return True
                        
                        l[i],l[i+num]  = 0, 0
                        vi[num] = False

            return False
            
        
        k = 2*n - 1
        l = [0] * k
        vi = [False]*(n+1)
        backtrack(l,0,vi)
        return l
                    
        
       
