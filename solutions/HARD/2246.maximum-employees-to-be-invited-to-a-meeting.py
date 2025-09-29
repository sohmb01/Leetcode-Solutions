# Problem ID: 2246
# Title: Maximum Employees to Be Invited to a Meeting
# Runtime: 330 ms

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Find longest cycle in the graph
        n = len(favorite)
        longestCycle = 0
        visited = set()
        cyclesWithLength2 = []
        for i in range(n):
            if i in visited:
                continue
            start, curr = i, i
            currVisited = set()
            while curr not in visited:
                visited.add(curr)
                currVisited.add(curr)
                curr = favorite[curr]

            if curr in currVisited:
                length = len(currVisited)
                while start != curr:
                    length -= 1
                    start = favorite[start]
                
                longestCycle = max(length, longestCycle)
                if length == 2:
                    cyclesWithLength2.append([curr,favorite[curr]])
                print(longestCycle)

        # Find sum of non closed components in the graph
        inverted = defaultdict(list)
        for i, num in enumerate(favorite):
            inverted[num].append(i)
        def bfs(node,parent):
            print(str(node)+" " + str(parent))
            q = deque([(node,0)])
            maxLength = 0
            while q:
                curr, length = q.popleft()
                if curr == parent:
                    continue
                maxLength = max(maxLength, length)
                for neighbor in inverted[curr]:
                    q.append((neighbor,length+1))
            return maxLength

        chainSum = 0
        for a,b in cyclesWithLength2:
            chainSum += bfs(a,b) + bfs(b,a) + 2
        
        return max(chainSum,longestCycle )