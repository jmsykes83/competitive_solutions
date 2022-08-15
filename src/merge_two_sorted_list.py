# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        sol = ListNode()
        
        if list1 == None and list2 == None:
            return list1
        
        while list1 != None:
            temp.append(list1.val)
            list1 = list1.next
            
        while list2 != None:
            temp.append(list2.val)
            list2 =  list2.next
        temp = reversed(sorted(temp))
        for x in temp:
            if(sol.val == 0 and sol.next == None):
                sol = ListNode(x)
                continue
            sol = ListNode(x, sol)
           
        return sol