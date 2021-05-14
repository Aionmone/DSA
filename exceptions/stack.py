from exceptions.base import Base

class StackFull(Base):
    '''Full stack exception'''
    def __init__(self, message='Stack has reached its full capacity.'):
        super().__init__(message)

class StackEmpty(Base):
    '''Empty stack exception'''
    def __init__(self, message='Stack is empty.'):
        super().__init__(message)