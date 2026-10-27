# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs (node, max so far) - returns the number of good nodes in that subtree
# base case:
# a node which is None adds nothing to the count, return 0
# recursive case:
# return 1 + () if you are <= max so far + left good count + right good count
# 


class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def help(node, max_so_far):
            if node is None:
                return 0

            tot = 0
            if node.val >= max_so_far:
                tot += 1


            val_for_max = max(node.val, max_so_far)

            tot += help(node.left, val_for_max)
            tot += help(node.right, val_for_max)

            return tot


        return help(root, float("-inf"))
        