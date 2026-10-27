# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curra = None
        currb = None
        curr = None
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            # start with list1
            curr = list1
            curra = list1.next
            currb = list2

        else:
            # start with list2
            curr = list2
            curra = list1
            currb = list2.next
        
        head = curr
            

        while curra and currb:
            if curra.val < currb.val:
                curr.next = curra
                curr = curr.next
                curra = curra.next 
            else:
                curr.next = currb
                curr = curr.next
                currb = currb.next

        if not curra:
            curr.next = currb 
        else:
            curr.next = curra

        
        return head

        