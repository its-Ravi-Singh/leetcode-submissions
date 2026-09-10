# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def trav(node):
            if node is None: return (0, 0)
            leftSum, leftCount = trav(node.left)
            rightSum, rightCount = trav(node.right)

            subTreeSum = leftSum + rightSum + node.val
            subTreeCount = leftCount + rightCount + 1

            if subTreeSum // subTreeCount == node.val: self.count += 1
            return (subTreeSum, subTreeCount)
        
        trav(root)
        return self.count