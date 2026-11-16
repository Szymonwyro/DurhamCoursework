def Merge4Way(L1,L2,L3,L4):
    """ Merge the four lists L1, L2, L3, L4 that are sorted
    in non-increasing order into a new list L that is
    sorted in non-increasing order, and return L """
    
def Merge4Sort(L):
    """ If L has at most one element, return L; if
    it has 2 to 4 elements, create a sorted list
    by a single call to Merge4Way; otherwise,
    make four recursive calls on sub-lists
    whose sizes differ by at most 1, and call Merge4Way
    to merge them. In either case, return a list
    that is a sorted version of L """
    
def q7_test():
    # Test for Merge4Way
    L1 = [8,6]
    L2 = [10]
    L3 = [9,5]
    L4 = [6,5]
    assert(Merge4Way(L1,L2,L3,L4)==[10,9,8,6,6,5,5])
    print("Merge4Way test passed")

    # Test for Merge4Sort
    L = [5,19,14,13,2,8,5,19,6]
    assert(Merge4Sort(L)==[19,19,14,13,8,6,5,5,2])
    print("Merge4Sort test passed")