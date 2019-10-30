"""
Math 590
Project 2
Fall 2019

p2stack.py

Partner 1: Simiao Ren
Partner 2: Yijun Mao
Date: 2019.10.26
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 100.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        self.size = size
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        #print("#el , size = ", self.numElems, self.size)
        return self.numElems == self.size

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        new_array = [None for x in range(0,2*self.size)]    #Create a new array with doubled size
        for i in range(self.size):                          #Get the old array into it using for loop
            new_array[i] = self.stack[i]
        self.stack = new_array                              #Change the stack pointer to the new array
        self.size *= 2                                      #Double the array size
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        if (self.isFull()):                   #Double the list if its full
            self.resize()
            #print("Your list is resized, the current length is ", self.size)
        self.top += 1                       #Increase the pointer
        self.stack[self.top] = val          #Plug in the value
        self.numElems += 1                  #Add the #el
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        if (self.numElems == 0):            #Check if it is empty now
            print("Warning: You are popping element from an empty stack, None will be poped out as a result")
            return None
        out = self.stack[self.top]          #Get the last val out
        self.stack[self.top] = None         #This is not necessary but just to make visually easier to debug
        self.top -= 1                       #Decrease the top pointer
        self.numElems -= 1                  #Decrease the numElems
        return out

#Write some test cases to test that the function is correctly implemented
if __name__ == '__main__':
    s1 = Stack(size = 1)
    for i in range(10):
        s1.push(i)
    for i in range(10):
        print(s1.pop())
    print(s1)
