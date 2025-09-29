# Problem ID: 93
# Title: Restore IP Addresses
# Runtime: 3 ms

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        octets = []
        ans = []

        def backtrack(start):
            if len(octets)==4 and start==len(s):
                ans.append(".".join(octets))
                return
            for i in range(1,4):
                octet = s[start:start+i]
                if len(octet)>1 and (octet[0]=="0" or int(octet)>255):
                    continue
                if len(octets)<4:
                    octets.append(octet)
                    backtrack(start+i)
                    octets.pop()
        
        backtrack(0)
        return ans
                    