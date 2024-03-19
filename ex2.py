import random

class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.data = value
        self.balance = 0  

class Tree:
    def __init__(self):
        self.root_node = None

    def add_node(self, value):
        if not self.root_node:
            self.root_node = Node(value)
        else:
            self.place_node(self.root_node, value, None)

    def place_node(self, current, value, parent):
        if not current:
            if value < parent.data:
                parent.left_child = Node(value)
            else:
                parent.right_child = Node(value)
            self.update_balance(parent)
        else:
            if value < current.data:
                self.place_node(current.left_child, value, current)
            else:
                self.place_node(current.right_child, value, current)

    def update_balance(self, node):
        if node:
            node.balance = self.node_height(node.left_child) - self.node_height(node.right_child)
            if node.balance > 1 or node.balance < -1:
                print(f"Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print(f"Case #1: Pivot not detected")
            self.update_balance(node.left_child)
            self.update_balance(node.right_child)

    def node_height(self, node):
        if not node:
            return 0
        return 1 + max(self.node_height(node.left_child), self.node_height(node.right_child))

# Test cases
def test_case(tree, values, case_description):
    print(f"\n{case_description}")
    for value in values:
        tree.add_node(value)

tree = Tree()
test_case(tree, [10], "Test Case 1: Adding a node results in case 1 (Pivot not detected)")

tree = Tree()
test_case(tree, [10, 5], "Test Case 2: Adding a node results in case 2 (Pivot exists but node is added to the shorter subtree)")

tree = Tree()
test_case(tree, [10, 5, 15, 20], "Test Case 3: Adding a node results in case 3 (not supported)")


