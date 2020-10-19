from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root is None

    def search_helper(self, node, key):
        if node is None:
            return False
        elif node.key == key:
            return True
        elif node.key < key:
            return self.search_helper(node.right, key)
        elif node.key > key:
            return self.search_helper(node.left, key)

    def search(self, key): # returns True if key is in a node of the tree, else False
        return self.search_helper(self.root, key)

    def insert_helper(self, node, key, data):
        if key < node.key:
            if node.left is not None:
                self.insert_helper(node.left, key, data)
            else:
                node.left = TreeNode(key, data)
        elif key > node.key:
            if node.right is not None:
                self.insert_helper(node.right, key, data)
            else:
                node.right = TreeNode(key, data)
        elif key == node.key:
            node.data = data


    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            return self.insert_helper(self.root, key, data)


    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        it = self.root
        while it.left is not None:
            it = it.left
        return(it.key, it.data)


    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        it = self.root
        while it.right is not None:
            it = it.right
        return (it.key, it.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            lefty = self.root
            l_count = 0
            r_count = 0
            while lefty.left is not None:
                l_count += 1
                lefty = lefty.left
            righty = self.root
            while righty.right is not None:
                r_count += 1
                righty = righty.right
            return max(l_count, r_count)

    def inorder_helper(self, node, l):
        if node is not None:
            self.inorder_helper(node.left, l)
            l.append(node.key)
            self.inorder_helper(node.right, l)
        return l

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        l = []
        return self.inorder_helper(self.root, l)

    def preorder_helper(self, node, l):
        if node is not None:
            l.append(node.key)
            self.inorder_helper(node.left, l)
            self.inorder_helper(node.right, l)
        return l

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        l = []
        return self.preorder_helper(self.root, l)

    def level_helper(self, node, n, q):

        if node is None:
            return q

        if n == 0:
            q.enqueue(node.key)


        lefty = self.level_helper(node.left, n - 1, q)
        righty = self.level_helper(node.right, n - 1, q)

        return lefty or righty

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        l = []
        x = 0
        if self.is_empty():
            return l
        else:
            height = self.tree_height()
            for i in range(height + 1):
                x = self.level_helper(self.root, i, q)
        for i in range(x.size()):
            l.append(x.dequeue())
        return l





