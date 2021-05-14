import unittest
from unittest.loader import makeSuite

from DSA import Stack
from exceptions import StackEmpty, StackFull

class StackTestCase(unittest.TestCase):
    '''Test case for Stack DSA'''

    def setUp(self):
        self.stack = Stack()
        self.__fill_stack()

    def test_push(self):
        '''Test for stack push'''
        with self.assertRaises(StackFull):
            self.stack.push(15)

        self.__empty_stack()
        self.assertIsNone(self.stack.push(1), msg='Should returns None')

    def test_pop(self):
        '''Test for stack pop'''
        self.assertEqual(self.stack.peek, self.stack.pop(), msg='Should returns last item')

        self.__empty_stack()
        with self.assertRaises(StackEmpty):
            self.stack.pop()

    def test_isEmpty(self):
        '''Test for stack isEmpty'''
        self.assertFalse(self.stack.isEmpty)

        self.__empty_stack()
        self.assertTrue(self.stack.isEmpty)

    def test_isFull(self):
        '''Test for stack isFull'''
        self.assertTrue(self.stack.isFull)

        self.__empty_stack()
        self.assertFalse(self.stack.isFull)

    def test_peek(self):
        '''Test for stack peek'''
        self.assertEqual(self.stack.peek, 14, msg='Should shows 1')

        self.__empty_stack()
        with self.assertRaises(StackEmpty):
            self.stack.peek

    def __empty_stack(self):
        '''Empty Stack for testing'''
        for i in range(0, len(self.stack)):
            self.stack.pop()

    def __fill_stack(self):
        '''Fill stack for testing'''
        for i in range(0, self.stack.capacity):
            self.stack.push(i)

if __name__ == '__main__':
    unittest.main()