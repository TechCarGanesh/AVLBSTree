from DLinkedList import *
VERTICAL = 1
HORIZONTAL = 0
MAX_HEIGHT = 16
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def left(self):
        return self.left

    def right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def data(self):
        return self.data

class BinarySearchTree:
    def __init__(self):
        self.parent = None
        self.level = 0
        self.nitems = 0

    def insert_bst(self, data):
        currentIndex = 0
        print("\n-->insert: ", data)
        if self.parent == None:
            self.parent = TreeNode(data)
            self.nitems += 1
            if self.level < self.Levelh(currentIndex):
                self.level = self.Levelh(currentIndex)
            return
        temp = self.parent
        while True:
            if data < temp.data:
                currentIndex = (2 * currentIndex + 1)
                print(" Left <<< ", currentIndex)
                if(temp.left == None):
                    temp.left = TreeNode(data)
                    self.nitems += 1
                    if self.level < self.Levelh(currentIndex):
                        self.level = self.Levelh(currentIndex)
                    break
                else:
                    temp = temp.left
            else:
                currentIndex = (2 * currentIndex + 2)
                print(" Right >>> ", currentIndex)
                if(temp.right == None):
                    temp.right = TreeNode(data)
                    self.nitems += 1
                    if self.level < self.Levelh(currentIndex):
                        self.level = self.Levelh(currentIndex)
                    break
                else:
                    temp = temp.right

    def inOrder(self, isVertical, qarray):
        currentIndex = 0
        cIndex = 0
        if self.parent != None:
            if isVertical == VERTICAL:
                self._inorderV(self.parent, currentIndex)
            else:
                self._inOrder(self.parent, currentIndex, qarray)

    def _inorderV(self, node, currentIndex):
        if node != None:
            currentIndex = 2 * currentIndex + 1
            self._inorderV(node.left, currentIndex)
            self.vLevel(currentIndex)
            print(node.data)
            currentIndex = 2 * currentIndex + 2
            self._inorderV(node.right, currentIndex)

    def fill_subtree(self, node, qarray, currentIndex):
        level = self.Levelh(currentIndex)
            # Left tree
        if self.nitems == 0:
            qarray[level].Append(-1)
            return
        if node.left == None or node.right == None:
            if level <= self.level:
                # Fill left subtree
                self.fill_subtree(node, qarray, ((2 * currentIndex) + 1))
                qarray[level].Append(-1)
                # right subtree
                self.fill_subtree(node, qarray, ((2 * currentIndex) + 2))

    def Levelh(self, currentIndex):
        level = 0
        while currentIndex != 0:
            currentIndex = (currentIndex - 1) // 2
            level += 1
        print("levelh ", level)
        return level

    def _inOrder(self, node, currentIndex, qarray):
        idx = self.Levelh(currentIndex)
        if node != None:
            # Fill the sub-tree with - if left or right is none
            if node.left == None:
                self.fill_subtree(node, qarray, ((currentIndex * 2) + 1))
            self._inOrder(node.left, ((currentIndex *2) + 1), qarray)
            print(node.data)
            qarray[idx].Append(node.data)
            self.nitems -= 1
            if node.right == None:
                self.fill_subtree(node, qarray, ((currentIndex * 2) + 2))
            self._inOrder(node.right, ((currentIndex * 2) + 2), qarray)
        else:
            print("curindex ", currentIndex, "level ", idx)

    # Simplified rotation for demonstration
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    # def balance(self, node):
    #     # This is a simplified version and may not fully balance the tree
    #     if self.height(node.left) > self.height(node.right):
    #         return self.rotate_right(node)
    #     else:
    #         return self.rotate_left(node)

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


    def height_difference(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)


# ===================================================
# Balancing a subtree
# ====================================================
    def tree_to_vine(self, root):
        vine_tail = root
        remainder = vine_tail.right
        vine_head = None

        while remainder is not None:
            if remainder.left is None:
                vine_tail = remainder
                remainder = remainder.right
            else:
                temp_ptr = remainder.left
                remainder.left = temp_ptr.right
                temp_ptr.right = remainder
                remainder = temp_ptr
                vine_tail.right = temp_ptr

                if vine_head is None:
                    vine_head = temp_ptr

        return vine_head

    def vine_to_tree(self, root, size):
        vine = root
        leaves = size + 1 - 2 ** (int(log(size + 1, 2)))
        vine = self.compress(vine, leaves)
        size -= leaves

        while size > 1:
            vine = self.compress(vine, size // 2)
            size //= 2

        return vine

    def compress(self, root, count):
        scanner = root

        for _ in range(count):
            small_node = scanner.right
            scanner.right = small_node.right
            scanner = scanner.right
            small_node.right = scanner.left
            scanner.left = small_node

        return root

    def balance(self):
        if self.parent is not None:
            self.parent = self.tree_to_vine(self.parent)
            self.parent = self.vine_to_tree(self.parent, self.size(self.parent))

    def size(self, parent):
        if parent is None:
            return 0
        else:
            return self.size(parent.left) + 1 + self.size(parent.right)

# ====================================================
# Done Balancing subtree
# ===================================================
# Create a BinarySearchTree object
bst = BinarySearchTree()
treeList = [DList() for _ in range(20)]
# Insert elements into the binary search tree
bst.insert_bst(1)
bst.insert_bst(2)
bst.insert_bst(3)
bst.insert_bst(4)
bst.insert_bst(5)
bst.insert_bst(6)
bst.insert_bst(7)
treeList = [DList() for _ in range(20)]
print("Height of the Binary Tree: ", bst.height(bst.parent))
print("Left subtree height: ", bst.height(bst.parent.left))
print("Right subtree height: ", bst.height(bst.parent.right))


# Now the tree is:
#       50
#      /  \
#    30    70
#   / \   /  \
# 20  40 60  80

# Now let's balance the tree
# bst.parent = bst.balance(bst.parent)
# #bst.rotate_left(bst.parent.right)
#
#
# print("After rotate")
#
#
# bst.parent = bst.balance(bst.parent)
# bst.parent = bst.balance(bst.parent)
# height = bst.height(bst.parent)
# mid = height // 2
# for i in range(0, mid):
#     bst.parent = bst.balance(bst.parent)
#
# print("Inorder (horizontal level)")
# bst.inOrder(HORIZONTAL, treeList)
# print("Vertical Tree")
# for i in range(bst.level + 1):
#     tlist = treeList[i]
#     # tlist.Output()
#     for node in iterDlist(tlist):
#         if node.data == -1:
#             print("-", end=' ')
#         else:
#             print(node.data, end=' ')
#     print('|')
#
# height = bst.height(bst.parent)
# mid = height // 2
# for i in range(0, mid):
#     bst.parent = bst.balance(bst.parent)

bst.balance()
print("Inorder (horizontal level)")
bst.inOrder(HORIZONTAL, treeList)
print("Vertical Tree")
for i in range(bst.level + 1):
    tlist = treeList[i]
    # tlist.Output()
    for node in iterDlist(tlist):
        if node.data == -1:
            print("-", end=' ')
        else:
            print(node.data, end=' ')
    print('|')

print("Height of the Binary Tree: ", bst.height(bst.parent))
print("Left subtree height: ", bst.height(bst.parent.left))
print("Right subtree height: ", bst.height(bst.parent.right))
# Please note that the balance method in this code is a simplified version and may not fully balance the tree.
