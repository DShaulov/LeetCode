import math
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Num = 0
        l1Iteration = 0
        while l1 != None:
            l1Num = l1Num + (l1.val * pow(10, l1Iteration))
            l1 = l1.next
            l1Iteration = l1Iteration + 1
        l2Num = 0
        l2Iteration = 0
        while l2 != None:
            l2Num = l2Num + (l2.val * pow(10, l2Iteration))
            l2 = l2.next
            l2Iteration = l2Iteration + 1
        totalNum = l1Num + l2Num
        print(totalNum)
        node = ListNode(totalNum % 10)
        totalNum = totalNum // 10
        nodeIterator = node
        while totalNum >= 1:
            lastDigit = totalNum % 10
            newNode = ListNode(lastDigit)
            nodeIterator.next = newNode
            nodeIterator = nodeIterator.next
            totalNum = totalNum // 10
        return node

if __name__ == "__main__":
    node1 = ListNode(2, ListNode(4, ListNode(3, None)))
    node2 = ListNode(5, ListNode(6, ListNode(4, None)))
    soltuion = Solution()
    soltuion.addTwoNumbers(node1, node2)
