# Test case for singly linked list

import unittest

from DSA import LinkedList

class LinkedListTestCase(unittest.TestCase):
    """Test case for LinkedList."""
    def setUp(self) -> None:
        self.list = LinkedList()

    def test_len(self):
        """Tests linked list len() function"""
        self.assertEqual(len(self.list), 0, "Should equal 0")
        self.__insert(5)
        self.assertEqual(len(self.list), 5, "Should equal 5")

    def test_iteration(self):
        """Test linked list iteration"""
        self.__insert(5)

        list_test = [num for num in range(5)]

        # Check with iter, next functions
        iter_list = iter(self.list)
        iter_test = iter(list_test)
        for num in list_test:
            self.assertEqual(next(iter_list), next(iter_test), f"Should equal {num}")

        # Check with for loop
        iter_test = iter(list_test)
        for data in self.list:
            test = next(iter_test)
            self.assertEqual(data, test, f"Should equal {test}")

    def test_insert(self):
        """Test LinkedList insert function"""
        # Empty insert
        self.assertIsNone(self.list.insert(0, 0))
        self.assertEqual(self.list.get(0), 0, "Should equal 0")

        # Insert at head
        self.assertIsNone(self.list.insert(1, 0))
        self.assertEqual(self.list.get(0), 1, "Should equal 0")

        # Insert at tail
        self.list.insert(2, len(self.list))
        self.assertEqual(self.list.get(2), 2, "Should equal 2")

        # Insert at middle
        self.assertIsNone(self.list.insert(3, 1))
        self.assertEqual(self.list.get(1), 3, "Should equal 3")

        # IndexError
        with self.assertRaises(IndexError, msg= "Should raises IndexError."):
            self.list.insert(5, 5)

    def test_delete(self):
        """Tests linked list delete method"""
        self.__insert(5)

        self.assertIsNone(self.list.delete(1), "Should return None.")
        self.assertEqual(len(self.list), 4, "Should equal 4.")

        with self.assertRaises(IndexError, msg= "Should rasies IndexError."):
            self.list.delete(6)

    def test_get(self):
        """Test linked list get method"""
        self.__insert(5)

        self.assertEqual(self.list.get(2), 2, "Should equal 2")
        self.assertIsNone(self.list.get(6), "Should returns None.")

    def test_display(self):
        """Test linked list display method"""
        self.__insert(5)

        list_test = tuple(num for num in range(5))
        self.assertEqual(self.list.display(), list_test, f"Should equal {list_test}")

    def __insert(self, items):
        """Insert items at tail of linked list"""
        for i in range(items):
            self.list.insert(i, len(self.list))
