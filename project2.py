"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *
from p2stack import *
from p2queue import *
from p2maze import *
"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""


def dfs(maze):
    s = Stack()
    s.push(maze.start)  # push the start into stack

    while not s.isEmpty():
        current = s.pop()
        if current.visited:  # Check if we visited this node
            continue
        current.visited = True  # Label it
        for nei in current.neigh:  # Loop through neighbour
            if nei.visited:
                continue
            s.push(nei)  # Push the neighbour
            nei.prev = current  # Get the previous
    return getpath(maze)


def bfs(maze):
    q = Queue()
    q.push(maze.start)  # Push the start of the maze
    maze.start.dist = 0 # label the start dist

    while not q.isEmpty():
        current = q.pop()

        for nei in current.neigh:
            if nei.dist != math.inf: # If this node has not been visited
                continue
            q.push(nei)         # Push it neighbour into it
            nei.dist =  current.dist + 1
            nei.prev = current
    return getpath(maze)


def getpath(maze):
    # Output path
    path_inv = []
    previous = maze.exit
    path_inv.append(maze.exit.rank)
    while not previous.isEqual(maze.start):
        path_inv.append(previous.rank)
        previous = previous.prev
    path_inv.append(maze.start.rank)  # Make up the start
    # invert the path from start -> exit
    path = path_inv[::-1]
    # print("last element in path is:", path[-1])
    # print("Exit node is:",maze.exit.rank)
    # print("Your inverse path is", path_inv)
    # print("Your Path is:", path)
    return path


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    if alg == 'DFS':
        return dfs(maze)
    else:
        return bfs(maze)


"""
Main function.
"""
if __name__ == "__main__":
    #m1 = Maze(0, True)
    #m1.printMat()
    #m1.printList()

    #m1.solve('DFS',True,False)
    testMazes(True)
