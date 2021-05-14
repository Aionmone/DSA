'''Base exception for DSA'''

class Base(Exception):
    '''Basic DSA exception'''
    def __init__(self, message):
        self.__message = message

        super().__init__(self.__message)

    def __str__(self):
        return self.__message
