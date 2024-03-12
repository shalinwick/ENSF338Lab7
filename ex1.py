import random
import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.data = value

class Tree:
    def __init__(self):
        self.root_node = None

    def add_node(self, value):
        if not self.root_node:
            self.root_node = Node(value)
        else:
            self.place_node(self.root_node, value)

    def place_node(self, current, value):
        if value < current.data:
            if not current.left_child:
                current.left_child = Node(value)
            else:
                self.place_node(current.left_child, value)
        else:
            if not current.right_child:
                current.right_child = Node(value)
            else:
                self.place_node(current.right_child, value)

    def find_value(self, value):
        return self.look_for_value(self.root_node, value)

    def look_for_value(self, current, value):
        if not current:
            return False
        if value == current.data:
            return True
        elif value < current.data:
            return self.look_for_value(current.left_child, value)
        else:
            return self.look_for_value(current.right_child, value)

    def node_height(self, node):
        if not node:
            return 0
        return 1 + max(self.node_height(node.left_child), self.node_height(node.right_child))

    def node_balance(self, node):
        if not node:
            return 0
        return self.node_height(node.left_child) - self.node_height(node.right_child)

    def deepest_imbalance(self, node):
        if not node:
            return 0
        return max(abs(self.node_balance(node)), self.deepest_imbalance(node.left_child), self.deepest_imbalance(node.right_child))


numbers_to_search = [list(range(1000)) for _ in range(1000)]
for number_list in numbers_to_search:
    random.shuffle(number_list)


balance_points = []
time_taken = []

for number_list in numbers_to_search:
    search_tree = Tree()
    for number in number_list:
        search_tree.add_node(number)
    
    timer_start = time.time()
    for number in number_list:
        search_tree.find_value(number)
    timer_end = time.time()
    
    time_for_search = (timer_end - timer_start) / len(number_list) * 1e6  # Multiplying by 1e^-6 is for dispaying the Y-Axis of search time in microseconds (more clarity)
    max_tree_balance = search_tree.deepest_imbalance(search_tree.root_node)
    
    balance_points.append(max_tree_balance)
    time_taken.append(time_for_search)


plt.figure(figsize=(10, 6))
plt.scatter(balance_points, time_taken, alpha=0.7, edgecolors='w', linewidth=0.5)
plt.xlabel('Max Node Balance')
plt.ylabel('Average Search Time (μs)')
plt.title('Tree Balance vs Search Performance')
plt.grid(True)
plt.tight_layout()
plt.show()
