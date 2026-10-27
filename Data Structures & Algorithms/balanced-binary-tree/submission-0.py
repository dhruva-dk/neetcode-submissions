# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# strategy
# each tree returns a tuple (balanced, height)
# base case: a tree with no nodes returns (true, 0)
# recursive: 
# two checks
# height is max(left, right) + 1
# balanced is abs(height_left - height_right) <= 1
# return (balanced, height)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node):
            if node is None:
                return (True, 0)

            #print(node)
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            height_here = max(left_height, right_height) + 1
            
            balanced = True
            if not left_balanced:
                balanced = False
            elif not right_balanced:
                balanced = False

            elif abs(left_height - right_height) > 1:
                balanced = False

            
            return (balanced, height_here)

        print(root)
        res = dfs(root)
        return res[0]
        