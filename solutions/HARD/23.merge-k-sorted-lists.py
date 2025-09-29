# Problem ID: 23
# Title: Merge k Sorted Lists
# Runtime: 2788 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        temp = head

        for l in lists:
            if l:
                heap.append(l.val)
        heapq.heapify(heap)
        
        while heap:
            val = heapq.heappop(heap)
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val == val:
                    temp.next = lists[i]
                    temp = temp.next

                    lists[i] = lists[i].next
                    
                    if lists[i]:
                        heapq.heappush(heap,lists[i].val)
        
        return head.next
                
