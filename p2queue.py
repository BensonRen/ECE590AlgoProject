"""
Math 590
Project 2
Fall 2019

p2queue.py

Partner 1: Simiao Ren
Partner 2: Yijun Mao
Date: 2019.10.26
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 100.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        self.size = size
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        return self.numElems == self.size

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        new_array = [None for x in range(0,2*self.size)]    # Create a new array with doubled size
        for i in range(self.size):                          # Get the old array into it using for loop
            new_array[i] = self.queue[(self.front + i)%self.size]
        self.queue = new_array                              # Change the queue pointer to the new array
        self.front = 0                                      # Cuz now first element in queue is at the front
        self.rear = self.size                               # The next available thing is the [prev_size] element
        self.size *= 2                                      # Double the array size
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        if self.isFull():                                   # Resize the queue if its full now
            print("Your queue is full, resizing to a bigger one with length", self.size * 2)
            self.resize()
        self.queue[self.rear % self.size] = val             # Get the queue element inside the queue
        self.rear += 1                                      # Increment the rear pointer and numEl
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        if self.isEmpty():                                  # Check if the queue is empty
            print("Warning: You are now popping from an empty queue, as a consequence you get None")
            return None
        out = self.queue[self.front % self.size]            # Take the first element out
        self.queue[self.front % self.size] = None           # Erase the original value, not necessary but good visually
        self.front += 1                                     # Increment the front pointer and decrement the size
        self.numElems -= 1
        return out





#Write some test cases to test that the function is correctly implemented
if __name__ == '__main__':
    s1 = Queue(size = 1)
    for i in range(10):
        s1.push(i)
    for i in range(10):
        print(s1.pop())
    print(s1)
