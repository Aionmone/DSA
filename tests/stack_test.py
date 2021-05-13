import unittest
from unittest.loader import makeSuite

from DSA import Stack
from exceptions import StackEmpty, StackFull

class TestStack(unittest.TestCase):
    '''Test case for Stack DSA'''

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        '''Test for stack push'''
        self.assertIsNone(self.stack.push(1), msg='Should returns None')
        
        self.__fill_stack(2)

        with self.assertRaises(StackFull):
            self.stack.push(16)

    def test_pop(self):
        '''Test for stack pop'''
        with self.assertRaises(StackEmpty):
            self.stack.pop()

        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1, msg='Should returns 1')

    def test_isEmpty(self):
        '''Test for stack isEmpty'''
        self.assertTrue(self.stack.isEmpty)

        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty)

    def test_isFull(self):
        '''Test for stack isFull'''
        self.assertFalse(self.stack.isFull)

        self.__fill_stack()
        self.assertTrue(self.stack.isFull)

    def test_peek(self):
        '''Test for stack peek'''
        self.stack.push(1)
        self.assertEqual(self.stack.peek, 1, msg='Should shows 1')

    def __fill_stack(self, start= 1, end= 16):
        '''Fill stack for testing'''
        for i in range(start, end):
            self.stack.push(i)

if __name__ == '__main__':
    unittest.main()