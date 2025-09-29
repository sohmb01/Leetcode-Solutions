# Problem ID: 3001
# Title: Apply Operations to Maximize Score
# Runtime: 3584 ms

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        points = 1
        primeScores = []
        for num in nums:
            score = 0
            for f in range(2, int(sqrt(num))+1):
                if num % f == 0:
                    score+=1
                    while num%f == 0:
                        num = num//f
            if num >= 2:
                score+=1
            primeScores.append(score)
        
        leftBounds = [-1] * n
        rightBounds = [n] * n
        
        st = []
        for i, s in enumerate(primeScores):
            while st and primeScores[st[-1]] < s:
                index = st.pop()
                rightBounds[index] = i
            if st:
                leftBounds[i] = st[-1]
            st.append(i)
        
        heap = [(-n,i) for i,n in enumerate(nums)]
        heapify(heap)

        while k > 0:
            n, i = heappop(heap)
            n = -n
            cnt = (i - leftBounds[i]) * (rightBounds[i] - i)
            operations = min(k,cnt)
            points = (points * pow(n,operations,MOD)) % MOD
            k-=operations
        return points
