# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input : a head of a binary tree, and a head of the subtree to look for
# output: boolean representing if the subtree is present

# strategy:
# recurse through the whole tree, and find nodes which are identical to the subroot
# if subroot is None, return true, all tress have a none subtree

# now that we have al ist of candidate roots
# dfs(node1, node2)
# base case: node1 is none or node2 is none: if both none, true, otherwise, false

# we know both are not none
# so return true to our caller if the 2 nodes have same value,
# dfs(lefts) == true and dfs(rights) == true


# quick trace:


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True


        # step 1: identify the candidates
        candidates = []
        target = subRoot.val
        def search_candidates(node):
            nonlocal target

            if node is None:
                return

            if node.val == target:
                candidates.append(node)

            search_candidates(node.left)
            search_candidates(node.right)

        search_candidates(root)

        # we have the candidates, now we need to dfs to validate them
        def validate_candidate(node1, node2):
            # node1 from main tree, node2 from subtree
            if not node1 or not node2:
                if not node1 and not node2:
                    return True

                return False
            
            return (node1.val == node2.val and 
                    validate_candidate(node1.left, node2.left) and 
                    validate_candidate(node1.right, node2.right))

        for candidate in candidates:
            if validate_candidate(candidate, subRoot):
                return True

        return False




        