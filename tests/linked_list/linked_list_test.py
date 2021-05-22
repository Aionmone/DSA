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

    def test_push(self):
        """Test LinkedList push method."""
        for i in range(5):
            self.assertIsNone(self.list.push(i))

        test_case = (4, 3, 2, 1, 0)
        self.assertEqual(self.list.display(), (4, 3, 2, 1, 0), f"Should equal {test_case}")

    def test_append(self):
        """Test LinkedList append method."""
        list_num = 5
        for i in range(list_num):
            self.assertIsNone(self.list.append(i))

        test_case = tuple(num for num in range(list_num))
        self.assertEqual(self.list.display(), test_case, f"Should equal {test_case}")

    def test_insert_after(self):
        """Test LinkedList insert function"""
        # Empty insert
        self.assertIsNone(self.list.insert_after(0, 0))
        self.assertEqual(self.list.get(0), 0, "Should equal 0")

        # Insert
        self.assertIsNone(self.list.insert_after(1, 0))
        self.assertEqual(self.list.get(1), 1, "Should equal 1")

        self.assertIsNone(self.list.insert_after(2, 0))
        self.assertEqual(self.list.get(1), 2, "Should equal 2")

        self.assertEqual(self.list.display(), (0, 2, 1), "Should equal (0, 2, 1)")

        # IndexError
        with self.assertRaises(IndexError, msg= "Should raises IndexError."):
            self.list.insert_after(5, 3)

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
            self.list.append(i)
