from exceptions.queue import QueueFull
import unittest

from DSA import CircularQueue
from exceptions import QueueEmpty, QueueFull

class CircularQueueTestCase(unittest.TestCase):
    """Test case for CircularQueue"""

    def setUp(self):
        """Set up queue for testing"""
        self.queue = CircularQueue()
    
    def test_enqueue(self):
        for i in range(self.queue.capacity):
            self.assertIsNone(self.queue.enqueue(i), "Shouldn't raise QueueFull error.")

        with self.assertRaises(QueueFull, msg="Should raise 'QueueFull' error."):
            self.queue.enqueue(10)

    def test_dequeue(self):
        self.__fill_queue()
        for i in range(len(self.queue)):
            self.assertEqual(self.queue.dequeue(), i, f"Should be equal to {i}.")

        with self.assertRaises(QueueEmpty, msg="Should raise 'QueueEmpty' error."):
            self.queue.dequeue()

    def test_isEmpty(self):
        """Test Queue isEmpty property"""
        self.assertTrue(self.queue.isEmpty(), "Should returns True.")

        self.queue.enqueue(0)
        self.assertFalse(self.queue.isEmpty(), "Should return False.")

    def test_isFull(self):
        """Test Queue isFull property"""
        self.assertFalse(self.queue.isFull(), "Should return False.")

        self.__fill_queue()
        self.assertTrue(self.queue.isFull(), "Should returns True.")

    def test_display(self):
        self.assertEqual(self.queue.display(), [None] * self.queue.capacity, f"Should be equal to {[None] * self.queue.capacity}.")

        queue = [None] * self.queue.capacity
        for i in range(self.queue.capacity):
            self.queue.enqueue(i)
            queue[i] = i
            self.assertEqual(self.queue.display(), queue, f"Should be equal to {queue}.")

    def test_peek(self):
        """Test Queue peek property"""
        self.__fill_queue()
        for i in range(self.queue.capacity):
            self.assertEqual(self.queue.peek, self.queue.dequeue(), f"Should be equal to {i}.")

        with self.assertRaises(QueueEmpty, msg="Should raise 'QueueEmpty' error."):
            self.queue.peek

    def __fill_queue(self):
        """Fills the queue for testing"""
        for i in range(self.queue.capacity):
            self.queue.enqueue(i)
