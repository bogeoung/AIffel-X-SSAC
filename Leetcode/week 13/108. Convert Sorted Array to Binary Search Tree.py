# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        # 중앙값을 구함(몫만 구함)
        mid = len(nums)//2

        # 구한 중앙값으로 루트 노드 생성
        node = TreeNode(nums[mid])
        # 정렬된 배열을 받았기 때문에 중앙 값 기준으로 나눠서 호출하면 됨.
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node