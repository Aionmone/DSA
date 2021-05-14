from exceptions.base import Base

class QueueFull(Base):
    '''Full Queue exception'''
    def __init__(self, message='Queue has reached its full capacity.'):
        super().__init__(message)

class QueueEmpty(Base):
    '''Empty Queue exception'''
    def __init__(self, message='Queue is empty.'):
        super().__init__(message)
