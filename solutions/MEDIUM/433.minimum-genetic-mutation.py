# Problem ID: 433
# Title: Minimum Genetic Mutation
# Runtime: 0 ms

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(startGene,0)])
        visit = set()
        while q:
            gene, dist = q.popleft()
            if gene == endGene:
                return dist
            for i in range(8):
                for c in "AGCT":
                    temp = gene[:i] + c + gene[i+1:]
                    if temp not in visit and temp in bank :
                        q.append((temp, dist+1))
                        visit.add(temp)
        return -1