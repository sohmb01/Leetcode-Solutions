# Problem ID: 876
# Title: Hand of Straights
# Runtime: 33 ms

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        keys = sorted(freq.keys())
        for key in keys:
            if freq[key] > 0:
                for i in range(1,groupSize):
                    if freq[key+i]<freq[key]:
                        return False
                    freq[key+i] -= freq[key]
        return True
