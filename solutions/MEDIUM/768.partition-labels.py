# Problem ID: 768
# Title: Partition Labels
# Runtime: 31 ms

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = [-1] * 26
        r = [-1] * 26
        for idx in range(len(s)):
            i = ord(s[idx])-ord('a')
            if l[i] == -1:
                l[i] = idx
                r[i] = idx
            else:
                r[i] = idx
        partitions = deque()
        partitions.append([-1,-1])
        size = 1
        
        for x in range(len(s)):
            i = ord(s[x])-ord('a')
            if l[i] == -1 and r[i] == -1:
                continue

            j = 0
            size = len(partitions)
            flag = True
            while j<size:
                partition = partitions[j]
                if not (partition[0]>r[i] or partition[1]<l[i]):
                    temp = [min(partition[0],l[i]),max(partition[1],r[i])]
                    partitions[j] = temp
                    flag = False
                    break
                j+=1

            if flag:
                partitions.append([l[i],r[i]])
        
        ans = []
        for i in range(1,len(partitions)):
            ans.append(partitions[i][1]-partitions[i][0]+1)
        return ans