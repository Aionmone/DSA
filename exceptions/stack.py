class Stack(Exception):
    '''Basic stack exception'''
    def __init__(self, message):
        self.__message = message

        super().__init__(self.__message)

    def __str__(self):
        return self.__message

class StackFull(Stack):
    '''Full stack exception'''
    def __init__(self, message='Stack has reached its full capacity.'):
        super().__init__(message)

class StackEmpty(Stack):
    '''Empty stack exception'''
    def __init__(self, message='Stack is empty.'):
        super().__init__(message)