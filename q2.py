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