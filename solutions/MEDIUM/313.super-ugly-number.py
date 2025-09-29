# Problem ID: 313
# Title: Super Ugly Number
# Runtime: 278 ms

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        l = len(primes)
        heap = []
        for prime in primes:
            heappush(heap, (prime,0,prime))
        out = [1]
        i = 1
        while i < n:
            val, idx, prime = heappop(heap)
            if out[-1] != val:
                out.append(val)
                i+=1
            heappush(heap,(out[idx+1]*prime, idx+1, prime))
        return out[n-1]