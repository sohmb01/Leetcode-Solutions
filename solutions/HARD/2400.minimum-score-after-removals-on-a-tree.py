# Problem ID: 2400
# Title: Minimum Score After Removals on a Tree
# Runtime: 3482 ms

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        totalXor = 0
        for x in nums:
            totalXor ^= x
        res = [float('inf')]

        def dfs(node, par):
            
            xor = nums[node]
            for child in adj[node]:
                if child == par:
                    continue
                xor ^= dfs(child,node)
            for child in adj[node]:
                if child == par:
                    dfs2(child, node, xor, node)
            return xor
        
        def dfs2(node, par, xor1, anc):
            xor2 = nums[node]
            for child in adj[node]:
                if child == par:
                    continue
                xor2 ^= dfs2(child,node,xor1, anc)
            if par == anc:
                return xor2
            res[0] = min(res[0],max(xor1,xor2,totalXor^xor1^xor2)-min(xor1,xor2,totalXor^xor1^xor2))
            return xor2

        dfs(0,-1)
        return res[0]
