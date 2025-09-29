# Problem ID: 638
# Title: Shopping Offers
# Runtime: 9 ms

class Solution:
    def findLowestPrice(self, price, special,needs):
        if tuple(needs) in self.d:
            return self.d[tuple(needs)]
        
        cost = 0
        #Dont take offer
        for need, p in zip(needs,price):
            cost += need * p
        
        # Take an offer
        for offer in special:
            for i, need in enumerate(needs):
                if need < offer[i]:
                    break
            else:
                updatedNeeds = [needs[i] - offer[i] for i in range(len(needs))]
                cost = min(cost, offer[-1]+self.findLowestPrice(price, special, updatedNeeds))
        self.d[tuple(needs)] = cost
        return cost


    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.d = {}
        return self.findLowestPrice(price, special,needs)
