# Test case for singly linked list

import unittest

from DSA import LinkedList

class LinkedListTestCase(unittest.TestCase):
    """Test case for LinkedList."""
    def setUp(self) -> None:
        self.list = LinkedList()
        self.test_cases = 5

    def test_len(self):
        """Tests linked list len() function"""
        self.assertEqual(len(self.list), 0, "Should equal 0")
        self.__insert(self.test_cases)
        self.assertEqual(len(self.list), 5, "Should equal 5")

    def test_contains(self):
        """Tests for key in linked list."""
        self.__insert(self.test_cases)

        for i in range(self.test_cases):
            self.assertTrue(i in self.list, "Should return True.")

        self.assertFalse(self.test_cases in self.list, "Should return False.")

    def test_getitem(self):
        """Test for list[key]"""
        self.__insert(self.test_cases)

        for i in range(self.test_cases):
            self.assertEqual(self.list[i], i, f"Should equal {i}")

        with self.assertRaisesRegex(IndexError, "Index out of range."):
            self.list[self.test_cases]

    def test_setitem(self):
        """Test for list[key] = value"""
        self.__insert(self.test_cases)

        for i in range(self.test_cases):
            self.list[i] = self.test_cases + i
            self.assertEqual(self.list[i], self.test_cases + i, f"Should equal {self.test_cases + i}")

        with self.assertRaisesRegex(IndexError, "Index out of range."):
            self.list[self.test_cases]

    def test_delitem(self):
        """Test for 'del list[key]'."""
        self.__insert(self.test_cases)

        del self.list[2]
        self.assertEqual(len(self.list), self.test_cases - 1,
            f"Length should equal {self.test_cases - 1}.")

        with self.assertRaisesRegex(IndexError, "Index out of range."):
            self.list[self.test_cases]

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
        test_cases = 5
        for i in range(test_cases):
            self.assertIsNone(self.list.push(i))

        list_test = [num for num in range((test_cases - 1), -1, -1)]
        self.assertEqual(self.list.display(), list_test, f"Should equal {list_test}")

    def test_insert(self):
        """Test LinkedList insert function"""
        pass

    def test_append(self):
        """Test LinkedList append method."""
        for i in range(self.test_cases):
            self.assertIsNone(self.list.append(i))

        list_test = [num for num in range(self.test_cases)]
        self.assertEqual(self.list.display(), list_test, f"Should equal {list_test}")

    def test_remove(self):
        """Tests linked list delete method"""
        pass

    def test_pop(self):
        """Test linked list pop method"""
        self.__insert(self.test_cases)
        list_test = [num for num in range(self.test_cases)]

        # Remove last item
        removed_item = list_test.pop()
        self.assertEqual(self.list.pop(), removed_item, f"Should equal {removed_item}")

        # Remove first item
        removed_item = list_test.pop(0)
        self.assertEqual(self.list.pop(0), removed_item, f"Should equal {removed_item}")

        # Remove from middle
        removed_item = list_test.pop(1)
        self.assertEqual(self.list.pop(1), removed_item, f"Should equal {removed_item}")

    def test_clear(self):
        """Test linked list clear method"""
        self.__insert(self.test_cases)
        self.list.clear()
        self.assertEqual(len(self.list), 0, "Should equal 0")

    def test_index(self):
        """Test linked list index method."""
        self.__insert(self.test_cases)

        for i in range(self.test_cases):
            self.assertEqual(self.list.index(i), i, f"Should equal {i}")

        with self.assertRaisesRegex(ValueError, f"Value '{self.test_cases}' not present."):
            self.list.index(self.test_cases)

    def test_get(self):
        """Test linked list get method"""
        self.__insert(5)

        self.assertEqual(self.list.get(2), 2, "Should equal 2")
        self.assertIsNone(self.list.get(6), "Should returns None.")

    def test_count(self):
        """Test linked list count method."""
        pass

    def test_reverse(self):
        """Test linked list reverse method."""
        pass

    def test_display(self):
        """Test linked list display method"""
        self.__insert(5)

        list_test = [num for num in range(5)]
        self.assertEqual(self.list.display(), list_test, f"Should equal {list_test}")

    def __insert(self, items):
        """Insert items at tail of linked list"""
        for i in range(items):
            self.list.append(i)
