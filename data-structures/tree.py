# To implement tree below
#        10
#      /    \
#    20     30
#   /  \      \
#  40  50     60
#     /  \
#    70  80

# The tree should also have the following traversal methods

# 1. In-order
# The printed result: 40, 20, 70, 50, 80, 10, 30, 60

# 2. Pre-order
# The printed result: 10, 20, 40, 50, 70, 80, 30, 60

# 3. Post-order
# The printed result: 40, 70, 80, 50, 20, 60, 30, 10


# The Tree class will be a wrapper for the Tree data structure
class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def count_nodes(self):
        # returns number of numbers within the tree
        if self.is_empty():
            return 0
        else:
            # to return the total count of nodes
            pass

    def in_order_traversal(self):
        # visit left subtree, visit current, visit right subtree
        if self.is_empty():
            print("Tree is empty.")
        else:
            self.root.in_order_traversal()

    def pre_order_traversal(self):
        # visit current, visit left subtree, visit right subtree
        if self.is_empty():
            print("Tree is empty.")
        else:
            self.root.pre_order_traversal()

    def post_order_traversal(self):
        # visit left subtree, visit right subtree, visit current
        if self.is_empty():
            print("Tree is empty.")
        else:
            self.root.post_order_traversal()

    def height(self):
        if self.is_empty():
            return 0
        else:
            return self.root.height() + 1

    def print_nodes_at_k_distance(self, k):
        if not self.is_empty():
            self.root.print_nodes_at_k_distance(k)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()

        print(self.data)

        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data)

        if self.left:
            self.left.pre_order_traversal()

        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()

        if self.right:
            self.right.post_order_traversal()

        print(self.data)

    def height(self):
        left_height = 0
        right_height = 0

        if self.left:
            left_height = 1 + self.left.height()

        if self.right:
            right_height = 1 + self.right.height()

        return max(left_height, right_height)

    def print_nodes_at_k_distance(self, k):
        if k == 0:
            print(self.data)

        if self.left:
            self.left.print_nodes_at_k_distance(k - 1)

        if self.right:
            self.right.print_nodes_at_k_distance(k - 1)


tree = Tree()
root = Node(10)
tree.root = root

node_1 = Node(20)
node_2 = Node(30)
root.left = node_1
root.right = node_2

node_3 = Node(40)
node_4 = Node(50)
node_5 = Node(60)
node_1.left = node_3
node_1.right = node_4
node_2.right = node_5

node_6 = Node(70)
node_7 = Node(80)
node_4.left = node_6
node_4.right = node_7

# tree.post_order_traversal()
# print(tree.height())
tree.print_nodes_at_k_distance(3)
