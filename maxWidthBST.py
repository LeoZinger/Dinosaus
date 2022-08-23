import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxWidth = 0

    def findMaxPathSum(self, node: TreeNode) -> int:
        def dfs(node: TreeNode, pathSum: int, level: int) -> int:
            if not node:
                return pathSum
            val_level = node.val
            for i in range(level):
                val_level = val_level * 10
            max_left = dfs(node.left, pathSum + val_level, level + 1)
            max_right = dfs(node.right, pathSum + val_level, level + 1)
            print("max_left = ", max_left)
            print("max_right = ", max_right)
            return max(max_left, max_right)
        return dfs(node, 0, 0)

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

    def bfs(self, root):
        q = [(root, 0)]
        while q:
            size = len(q)
            self.maxWidth = max(self.maxWidth, q[-1][1] - q[0][1] + 1)

            for i in range(size):
                node, pos = q.pop(0)
                if node.left:
                    q.append((node.left, 2 * pos + 1))
                if node.right:
                    q.append((node.right, 2 * pos + 2))


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

solution = Solution()
# print("Height of tree = ", solution.findTreeHeight(root))
solution.bfs(root)
print("Max Width Of BinaryTree = ", solution.maxWidth)
print("Max PathSum - root leftmost number - Of BinaryTree = ", solution.findMaxPathSum(root))

