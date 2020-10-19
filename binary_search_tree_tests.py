import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        #self.assertEqual(bst.level_order_list(), [10])

    def test_empty(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(10))
        bst.insert(20, "k")
        bst.insert(5, "k")
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(7))

    def test_min_max(self):
        bst = BinarySearchTree()
        bst.insert(20, "k")
        bst.insert(10, "yer")
        bst.insert(30, "idk")
        bst.insert(5, "l")
        self.assertEqual(bst.find_min(), (5, 'l'))
        self.assertEqual(bst.find_max(), (30, 'idk'))

    def test_height(self):
        r = BinarySearchTree()
        self.assertIsNone(r.tree_height())
        r.insert(20, "yssir")
        r.insert(30, "f")
        r.insert(5, "j")
        r.insert(4, "c")
        r.insert(67, "k")
        self.assertEqual(2, r.tree_height())

    def test_list_order(self):
        r = BinarySearchTree()
        self.assertEqual(r.level_order_list(), [])
        r.insert(10, "yssir")
        r.insert(20, "f")
        r.insert(5, "b")
        r.insert(3, "l")
        r.insert(25, "f")
        self.assertEqual(r.level_order_list(), [10, 5, 20, 3, 25])



if __name__ == '__main__': 
    unittest.main()
