from dataclasses import dataclass

@dataclass
class Node:
    """Implements a node from a (singly) linked grid.
    For a Node n:
        n.data holds an integer value
        n.nextX refers to the next Node horizontally in the linked grid, or None
        n.nextY refers to the next Node vertically in the linked grid, or None
    You must not modify this code.
    """
    data: int
    nextX: 'Node' = None
    nextY: 'Node' = None

@dataclass
class LinkedGrid:
    """Implements a (singly) linked grid.
    You must not modify this code.
    """
    head: Node = None
    sizeX: int = 0
    sizeY: int = 0

#### WRITE YOUR SOLUTION BELOW; DO NOT MODIFY CODE ABOVE THIS LINE####
#### COPY YOUR CODE FROM BELOW INTO A FILE q2.py FOR SUBMISSION ####
#### DO NOT INCLUDE CODE ABOVE THIS LINE IN q2.py ####

def fetch(linked_grid, i, j):
    """Returns the data at position (i, j) in the linked grid; i.e. the data held in the ith row and the jth column.
    Note: i and j are 1-indexed. fetch(linked_grid, 1, 1) returns the data in the head node.
    """
    raise NotImplementedError("Implement this function")


def equal_values(linked_grid_a, linked_grid_b):
    """Returns True if the two linked grids have the same dimensions
    and if for position (i,j) both linked grids have the same value.
    """
    raise NotImplementedError("Implement this function")

def extract_row(linked_grid,i):
    """Removes row i from the input linked grid and
    returns a new linked grid consisting of that row i
    """
    raise NotImplementedError("Implement this function")

def extract_column(linked_grid,j):
    """Removes column j from the input linked grid and
    returns a new linked grid consisting of that column j
    """
    raise NotImplementedError("Implement this function")
    
def transpose(linked_grid):
    """Returns the transpose of the input linked grid.
    May modify the input linked grid."""
    raise NotImplementedError("Implement this function")

def element_wise_multiply(linked_grid_a, linked_grid_b):
    """Returns a linked grid which is the element-wise product of the two input linked grids.
    Assumes the two input linked grids have the same dimensions. May modify inputs."""
    raise NotImplementedError("Implement this function")


#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q2.py ####


def q2_test_grid():
    # create a 3 x 3 grid
    # 1 2 3
    # 4 5 6
    # 7 8 9
    N1 = Node(data=1)
    N2 = Node(data=2)
    N3 = Node(data=3)
    N4 = Node(data=4)
    N5 = Node(data=5)
    N6 = Node(data=6)
    N7 = Node(data=7)
    N8 = Node(data=8)
    N9 = Node(data=9)
    N1.nextX = N2
    N1.nextY = N4
    N2.nextX = N3
    N2.nextY = N5
    N3.nextX = None
    N3.nextY = N6
    N4.nextX = N5
    N4.nextY = N7
    N5.nextX = N6
    N5.nextY = N8
    N6.nextX = None
    N6.nextY = N9
    N7.nextX = N8
    N7.nextY = None
    N8.nextX = N9
    N8.nextY = None
    N9.nextX = None
    N9.nextY = None
    return LinkedGrid(head=N1, sizeX=3, sizeY=3)

# Some basic tests
def q2_simple_tests():
    # test fetch
    T = q2_test_grid()
    assert(fetch(T,1,1)==1)
    assert(fetch(T,3,1)==7)
    assert(fetch(T,3,3)==9)

    # test equal_values
    T1 = q2_test_grid()
    T2 = q2_test_grid()
    assert(equal_values(T1,T2)==True)
    T2.head.nextX.nextY.data=99
    assert(equal_values(T1,T2)==False)

    # test extract_row
    T = q2_test_grid()
    R2 = extract_row(T,2)
    assert(T.sizeX==3)
    assert(T.sizeY==2)
    assert(R2.sizeX==3)
    assert(R2.sizeY==1)
    assert(T.head.nextX.nextX.nextY.data==9)
    assert(R2.head.nextX.data==5)

    # test extract_column
    T = q2_test_grid()
    C2 = extract_column(T,1)
    assert(T.sizeX==2)
    assert(T.sizeY==3)
    assert(C2.sizeX==1)
    assert(C2.sizeY==3)
    assert(T.head.data==2)
    assert(C2.head.nextY.data==4)

    # test transpose
    T = q2_test_grid()
    TT = transpose(T)
    assert(TT.sizeX==3)
    assert(TT.sizeY==3)
    assert(TT.head.nextY.data==2)
    assert(TT.head.nextX.nextX.data==7)

    # Test element-wise multiplication
    T1 = q2_test_grid()
    T2 = q2_test_grid()
    R = element_wise_multiply(T1,T2)
    assert(R.sizeX==3)
    assert(R.sizeY==3)
    assert(R.head.nextX.nextY.data == 25)
    assert(R.head.nextX.nextX.nextY.nextY.data == 81)

