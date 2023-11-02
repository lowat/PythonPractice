class Solution(object):
    def maxDepth(self, root):
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0
        return 1 + max(self.dfs(node.left), self.dfs(node.right))