# Problem ID: 322
# Title: Coin Change
# Runtime: 916 ms

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = [10001]*(amount+1)
        l[0] = 0
        for i in range(1,len(l)):
            if i in coins:
                l[i] = 1
            else:
                for coin in coins:
                    if i-coin>0:
                        if l[i-coin] == 10001:
                            continue
                        l[i] = min(l[i],l[i-coin]+1)

              
        return -1 if l[amount]==10001 else l[amount]
