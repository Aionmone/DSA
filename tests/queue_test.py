import unittest

from DSA.queue import Queue
from exceptions.queue import QueueEmpty, QueueFull

class QueueTestCase(unittest.TestCase):
    '''Test case for Queue data structure'''

    def setUp(self):
        '''Setting up queue for tests'''
        self.queue = Queue()
        self.__fill_queue()

    def test_enqueue(self):
        '''Test for enqueue method'''
        with self.assertRaises(QueueFull):
            self.queue.enqueue(17)
        
        self.__empty_queue()
        self.assertIsNone(self.queue.enqueue(16))

    def test_dequeue(self):
        '''Test for dequeue method'''
        self.assertEqual(self.queue.peek, self.queue.dequeue())

        self.__empty_queue()
        with self.assertRaises(QueueEmpty):
            self.queue.dequeue()

    def test_isEmpty(self):
        '''Test Queue isEmpty property'''
        self.assertFalse(self.queue.isEmpty)

        self.__empty_queue()
        self.assertTrue(self.queue.isEmpty)

    def test_isFull(self):
        '''Test Queue isFull property'''
        self.assertTrue(self.queue.isFull)

        self.__empty_queue()
        self.assertFalse(self.queue.isFull)

    def test_peek(self):
        '''Test Queue peek property'''
        self.assertEqual(self.queue.peek, 0)

        self.__empty_queue()
        with self.assertRaises(QueueEmpty):
            self.queue.peek

    # Private methods
    def __set_capacity(self, capacity= 15):
        '''Set the capacity of Queue'''
        self.queue.capacity = capacity

    def __empty_queue(self):
        '''Empty the Queue ofr testing'''
        for i in range(0, len(self.queue)):
            self.queue.dequeue()

    def __fill_queue(self):
        '''Fills the queue for testing'''
        self.__set_capacity()

        for i in range(0, self.queue.capacity):
            self.queue.enqueue(i)
