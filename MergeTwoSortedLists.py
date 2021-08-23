from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        myNode = None
        if l1.val <= l2.val:
            myNode = l1
            l1 = l1.next
        else:
            myNode = l2
            l2 = l2.next
        firstNode = myNode
        while True:
            if l1 == None and l2 == None:
                return firstNode
            elif l1 == None:
                while l2 != None:
                    myNode.next = l2
                    l2 = l2.next
                    myNode = myNode.next
                return firstNode
            elif l2 == None:
                while l1 != None:
                    iteratorNode = l1
                    l1 = l1.next
                    myNode = myNode.next
                return firstNode
            else:
                if l1.val <= l2.val:
                    myNode.next = l1
                    l1 = l1.next
                    myNode = myNode.next
                else :
                    myNode.next = l2
                    l2 = l2.next
                    myNode = myNode.next
            
if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode()
    node1.val = 1
    node1.next = ListNode()
    node1.next.val = 2
    node1.next.next = ListNode()
    node1.next.next.val = 4
    node2 = ListNode()
    node2.val = 1
    node2.next = ListNode()
    node2.next.val = 3
    node2.next.next = ListNode()
    node2.next.next.val = 4
    node = solution.mergeTwoLists(node1, node2)
    while node != None:
        print(node.val)
        node = node.next

                    
                