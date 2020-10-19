
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.count = 0
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.count == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.count == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError
        else:
            self.count += 1
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError
        else:
            self.count -= 1
            ret = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            return ret



    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.count
    
