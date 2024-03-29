# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head= v3 = ListNode()
        while list1  and list2 :
            if list1 and list2:
                if list1.val > list2.val:
                    v3.next = list2
                    list2 = list2.next
                else:
                    v3.next = list1
                    list1 = list1.next
            v3 = v3.next
        v3.next = list1 if(list1 != None) else list2
        return head.next
        
        
        