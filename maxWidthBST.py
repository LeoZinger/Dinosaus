# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
        height = self.findTreeHeight(root)
        current_height = 1
        queue = [root]
        max_width = 0
        bfs_list = []
        while queue:
            bfs_list.clear()
            for i in range(len(queue)):
                current_node = queue.pop(0)
                # if current_node.val != float('inf'):
                bfs_list.append(current_node.val)
                if current_height < height:
                    if not current_node.left:
                        new_node = TreeNode(float('inf'))
                        current_node.left = new_node
                    if not current_node.right:
                        new_node = TreeNode(float('inf'))
                        current_node.right = new_node
                middle = False
                width = 0
                for j in range(len(bfs_list)):
                    if bfs_list[j] != float('inf'):
                        middle = True
                        width += 1
                    if bfs_list[j] == float('inf') and middle:
                        width += 1
                max_width = max(max_width, width)
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
