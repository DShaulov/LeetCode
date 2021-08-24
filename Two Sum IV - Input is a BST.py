from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root == None:
            return False
        numList = []
        self.traverseTree(root, numList)
        print(numList)
        for i in range(len(numList)):
            for j in range(len(numList)):
                if j == i:
                    continue
                if numList[i] + numList[j] == k:
                    return True
        return False
    def traverseTree(self, root: Optional[TreeNode], ls: list):
        if root.left != None:
            self.traverseTree(root.left, ls)
        ls.append(root.val)
        if root.right != None:
            self.traverseTree(root.right, ls)

if __name__ == "__main__":
    solution = Solution()
    node1 = TreeNode(5, None, None)
    node1.left = TreeNode(3, None, None)
    node1.left.left = TreeNode(2, None, None)
    node1.left.right = TreeNode(4, None, None)
    node1.right = TreeNode(6, None, None)
    node1.right.right = TreeNode(7, None, None)
    print(solution.findTarget(node1, 9))
