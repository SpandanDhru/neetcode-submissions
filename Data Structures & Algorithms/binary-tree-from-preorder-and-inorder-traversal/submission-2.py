# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: i for i, val in enumerate(inorder)}

        def build(pre_start, in_start, in_end):
            if in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            mid = indices[root_val]
            left_size = mid - in_start

            root.left = build(pre_start + 1, in_start, mid - 1)
            root.right = build(pre_start + left_size + 1, mid + 1, in_end)

            return root
        return build(0, 0, len(inorder) - 1)

        
        