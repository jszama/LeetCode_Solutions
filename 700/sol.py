# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        if root.val == val:
            ans = TreeNode()
            ans.val, ans.left, ans.right = root.val, root.left, root.right
            return ans
        if root.val > val:
            return self.searchBST(root.left, val) 
        else:
            return self.searchBST(root.right, val) 
