# Problem ID: 2026
# Title: Merge Triplets to Form Target Triplet
# Runtime: 29 ms

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = False,False,False

        for triplet in triplets:
            if triplet[0]==target[0] and triplet[1]<=target[1] and triplet[2]<=target[2]:
                a = True
            if triplet[0]<=target[0] and triplet[1]==target[1] and triplet[2]<=target[2]:
                b= True
            if triplet[0]<=target[0] and triplet[1]<=target[1] and triplet[2]==target[2]:
                c = True
        return a and b and c
            