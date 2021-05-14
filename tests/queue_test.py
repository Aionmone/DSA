import unittest

from DSA.queue import Queue
from exceptions.queue import QueueEmpty, QueueFull

class QueueTestCase(unittest.TestCase):
    '''Test case for Queue data structure'''

    def setUp(self):
        '''Setting up queue for tests'''
        self.queue = Queue()
        self.__set_capacity()

    def test_enqueue(self):
        '''Test for enqueue method'''
        for i in range(self.queue.capacity):
            self.assertIsNone(self.queue.enqueue(i))

        with self.assertRaises(QueueFull):
            self.queue.enqueue(15)

    def test_dequeue(self):
        '''Test for dequeue method'''
        self.__fill_queue()
        for i in range(len(self.queue)):
            self.assertEqual(self.queue.dequeue(), i)

        with self.assertRaises(QueueEmpty):
            self.queue.dequeue()

    def test_isEmpty(self):
        '''Test Queue isEmpty property'''
        self.assertTrue(self.queue.isEmpty())

        self.queue.enqueue(0)
        self.assertFalse(self.queue.isEmpty())

    def test_isFull(self):
        '''Test Queue isFull property'''
        self.assertFalse(self.queue.isFull())

        self.__fill_queue()
        self.assertTrue(self.queue.isFull())

    def test_peek(self):
        '''Test Queue peek property'''
        self.__fill_queue()
        while len(self.queue) >= 1:
            self.assertEqual(self.queue.peek, self.queue.dequeue())

        with self.assertRaises(QueueEmpty):
            self.queue.peek

    # Private methods
    def __set_capacity(self, capacity= 15):
        '''Set the capacity of Queue'''
        self.queue.capacity = capacity

    def __fill_queue(self):
        '''Fills the queue for testing'''
        for i in range(self.queue.capacity):
            self.queue.enqueue(i)
