import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def findTreeHeight(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self.findTreeHeight(node.left) + 1, self.findTreeHeight(node.right) + 1)

    def bfsTraverse(self, root: TreeNode):
        if not root:
            return
        queue = [root]
        print("BFS Traverse: ", end=' ')
        while queue:
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                print(curr_node.val, end=' ')
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        # height = self.findTreeHeight(root)
        # current_height = 1
        curr_q = [root]
        next_q = []
        max_width = 0
        while curr_q:
            for i in range(len(curr_q)):
                curr_node = curr_q[i]
                if curr_node.left:
                    # print("curr_node.left val : ", curr_node.left.val)
                    next_q.append(curr_node.left)
                if curr_node.right:
                    # print("curr_node.left val : ", curr_node.right.val)
                    next_q.append(curr_node.right)
            # print("curr_q list type : ", type(curr_q))
            # print("next_q list type : ", type(next_q))
            for i in range(len(next_q)):
                next_node = next_q[i]
                print("next_q[", i, "] : ", next_node.val)
            curr_width = 0
            width_start = False
            for curr_node in curr_q:
                if (curr_node.left or curr_node.right) == next_q[0] \
                        and not width_start:
                    width_start = True
                    curr_width += 1
                if curr_node.left != next_q[len(next_q)-1] and curr_node.right != next_q[len(next_q)-1] \
                        and width_start:
                    curr_width += 2
                if (curr_node.left == next_q[len(next_q)-1] or curr_node.right == next_q[len(next_q)-1]) \
                        and width_start:
                    curr_width += 1
                    break
            max_width = max(max_width, curr_width)

            curr_q.clear()
            curr_q = next_q
            next_q.clear()
        return max_width

        def findTreeHeight(node: TreeNode) -> int:
            if not node:
                return 0
            return max(findTreeHeight(node.left) + 1, findTreeHeight(node.right) + 1)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

solution = Solution()
# print("Height of tree = ", solution.findTreeHeight(root))
solution.bfsTraverse(root)
print("Max Width Of BinaryTree = ", solution.widthOfBinaryTree(root))
