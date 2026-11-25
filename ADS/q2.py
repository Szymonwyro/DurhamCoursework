from q2_supplementary.py import Node, LinkedGrid

def fetch(linked_grid, i, j):
    """Returns the data at position (i, j) in the linked grid; i.e. the data held in the ith row and the jth column.
    Note: i and j are 1-indexed. fetch(linked_grid, 1, 1) returns the data in the head node.
    """
    i_value = linked_grid.head

    if i == 1:
        pass
    else:
        for i in range(1,i):
            i_value = i_value.nextX

    j_value = i_value

    if j == 1:
        pass
    else:
        for j in range(1,j):
            j_value = i_value.nextY
    
    return j_value.data


def equal_values(linked_grid_a, linked_grid_b):
    countax = 0
    countay = 0
    countbx = 0
    countby = 0

    ax = linked_grid_a.head
    ay = linked_grid_a.head

    if linked_grid_a.head == None:
        pass
    else:
        while ax.nextX != None:
            countax += 1
            ax = ax.nextX
        size_ax = countax + 1
        while ay.nextY != None:
            countay += 1
            ay = ay.nextY
        size_ay = countax + 1

    bx = linked_grid_b.head
    by = linked_grid_b.head

    if linked_grid_b.head == None:
            pass
    else:
        while bx.nextX != None:
            countbx += 1
            bx = bx.nextX
        size_bx = countbx + 1
        while by.nextY != None:
            countby += 1
            by = by.nextY
        size_by = countby +1

    return [size_ax, size_ay] == [size_bx, size_by]

def extract_row(linked_grid,i):     
    """Removes row i from the input linked grid and
    returns a new linked grid consisting of that row i
    """
    if i == 1:
        extracted_start = linked_grid.head          # for top row, the start of the extracted row is going to be the start of the original   
        linked_grid.head = extracted_start.nextY    # for top row, the rest of the grid will start at the node below the original head
        new_node = extracted_start                  # new node iterates through the extracted row, removing its links to the original grid

        while new_node is not None:
            new_node.nextY = None
            new_node = new_node.nextX
    else:
        # we need to take the row above the extracted one, and have its nextY's skip over the extracted row.
        above = linked_grid.head
        below = above.nextY.nextY
        for j in range(i - 2):
            above = above.nextY
            below = below.nextY

        while above is not None:
            above.nextY = below
            above = above.nextX
            if below is not None:
                below = below.nextX

        extracted_start = above.nextY
        node = extracted_start
        while node is not None:
            node.nextY = None
            node = node.nextX

    return LinkedGrid(extracted_start, linked_grid.sizeX, 1)
        

            

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