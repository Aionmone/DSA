import unittest
from unittest.loader import makeSuite

from DSA import Stack
from exceptions import StackEmpty, StackFull

class StackTestCase(unittest.TestCase):
    '''Test case for Stack DSA'''

    def setUp(self):
        self.stack = Stack()
        # self.__fill_stack()

    def test_push(self):
        '''Test for stack push'''
        for i in range(0, self.stack.capacity):
            self.assertIsNone(self.stack.push(i), msg="Shouldn't raise StackFull error")
        
        with self.assertRaises(StackFull):
            self.stack.push(15)

    def test_pop(self):
        '''Test for stack pop'''
        self.__fill_stack()
        for i in range(len(self.stack)):
            i += 1
            i = self.stack.capacity - i
            self.assertEqual(self.stack.pop(), i, msg="Shouldn't raise StackEmpty error")

        with self.assertRaises(StackEmpty):
            self.stack.pop()

    def test_isEmpty(self):
        '''Test for stack isEmpty'''
        self.assertTrue(self.stack.isEmpty())

        self.stack.push(0)
        self.assertFalse(self.stack.isEmpty())

    def test_isFull(self):
        '''Test for stack isFull'''
        self.assertFalse(self.stack.isFull())

        self.__fill_stack()
        self.assertTrue(self.stack.isFull())

    def test_peek(self):
        '''Test for stack peek'''
        self.__fill_stack()
        while len(self.stack) >= 1:
            self.assertEqual(self.stack.peek, self.stack.pop(), msg='Should returns equal')

        self.assertIsNone(self.stack.peek, "Should returns None.")

    def __fill_stack(self):
        '''Fill stack for testing'''
        for i in range(self.stack.capacity):
            self.stack.push(i)

if __name__ == '__main__':
    unittest.main()