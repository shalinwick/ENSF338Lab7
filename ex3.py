import random

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
        self.diff = 0
        self.depth = 1

class BalancedTree:
    def __init__(self):
        self.base = None

    def insert(self, value):
        if not self.base:
            self.base = TreeNode(value)
        else:
            self.base = self._insert_into_position(self.base, value)

    def _insert_into_position(self, node, value):
        if not node:
            return TreeNode(value)
        
        if value < node.val:
            node.left = self._insert_into_position(node.left, value)
        else:
            node.right = self._insert_into_position(node.right, value)
        
        return self._adjust_tree(node)

    def _update_depth_and_diff(self, node):
        depth_left = self._get_depth(node.left)
        depth_right = self._get_depth(node.right)
        node.depth = 1 + max(depth_left, depth_right)
        node.diff = depth_left - depth_right

    def _rotate_left(self, root):
        new_root = root.right
        subtree = new_root.left

        new_root.left = root
        root.right = subtree

        self._update_depth_and_diff(root)
        self._update_depth_and_diff(new_root)

        return new_root

    def _rotate_right(self, root):
        new_root = root.left
        subtree = new_root.right

        new_root.right = root
        root.left = subtree

        self._update_depth_and_diff(root)
        self._update_depth_and_diff(new_root)

        return new_root

    def _adjust_tree(self, node):
        self._update_depth_and_diff(node)
        
        
        if node.diff > 1 and node.left.diff >= 0:
            print("Case #3a: adding a node to an outside subtree")
            return self._rotate_right(node)
        
        
        if node.diff < -1 and node.right.diff <= 0:
            print("Complex Right-Left Case")
            return self._rotate_left(node)
        
        
        if node.diff > 1 and node.left.diff < 0:
            node.left = self._rotate_left(node.left)
            print("Complex Left-Right Case")
            return self._rotate_right(node)
        
        
        if node.diff < -1 and node.right.diff > 0:
            node.right = self._rotate_right(node.right)
            print("Case 3b not supported")
            return self._rotate_left(node)
        
        return node

    def _get_depth(self, node):
        if not node:
            return 0
        return node.depth


def perform_test(tree, values, description):
    print(f"\n{description}")
    for value in values:
        tree.insert(value)


b_tree = BalancedTree()
perform_test(b_tree, [30, 20, 10], "Test Case: #1")

b_tree = BalancedTree()
perform_test(b_tree, [30, 40, 35], "Test Case: #2")
