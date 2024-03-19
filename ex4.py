import random

class BinaryTreeElement:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
        self.equilibrium = 0
        self.tallness = 1

class BalancedBinaryTree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        if not self.root:
            self.root = BinaryTreeElement(value)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return BinaryTreeElement(value)
        
        if value < node.val:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        
        return self._ensure_balance(node)

    def _update_dimensions(self, element):
        left_tallness = self._determine_height(element.left)
        right_tallness = self._determine_height(element.right)
        element.tallness = 1 + max(left_tallness, right_tallness)
        element.equilibrium = left_tallness - right_tallness

    def _pivot_left(self, root):
        new_root = root.right
        transferred_subtree = new_root.left

        new_root.left = root
        root.right = transferred_subtree

        self._update_dimensions(root)
        self._update_dimensions(new_root)

        return new_root

    def _pivot_right(self, root):
        new_root = root.left
        transferred_subtree = new_root.right

        new_root.right = root
        root.left = transferred_subtree

        self._update_dimensions(root)
        self._update_dimensions(new_root)

        return new_root

    def _pivot_left_right(self, node):
        node.left = self._pivot_left(node.left)
        return self._pivot_right(node)

    def _pivot_right_left(self, node):
        node.right = self._pivot_right(node.right)
        return self._pivot_left(node)

    def _ensure_balance(self, node):
        self._update_dimensions(node)
        
        if node.equilibrium > 1 and node.left.equilibrium >= 0:
            return self._pivot_right(node)
        
        if node.equilibrium < -1 and node.right.equilibrium <= 0:
            return self._pivot_left(node)
        
        if node.equilibrium > 1 and node.left.equilibrium < 0:
            return self._pivot_left_right(node)
        
        if node.equilibrium < -1 and node.right.equilibrium > 0:
            return self._pivot_right_left(node)
        
        return node

    def _determine_height(self, node):
        if not node:
            return 0
        return node.tallness

def evaluate_test_cases(btree, entries, scenario):
    print(f"\n{scenario}")
    for entry in entries:
        btree.insert_value(entry)


binary_tree = BalancedBinaryTree()
evaluate_test_cases(binary_tree, [30, 20, 25], "Test Case 6: Left-Right Rotation")

binary_tree = BalancedBinaryTree()
evaluate_test_cases(binary_tree, [30, 40, 35], "Test Case 7: Right-Left Rotation")
