def hash_linear(d):
    """Inserts/deletes keys from the list d into a hash table
    and returns the HashTable which contains the state of the 
    hash table after these insertions. Positive values in d
    are insertions, negative values deletions.

    Use just one HashTable instance inside this function.
    
    Uses linear probing to resolve collisions.

    Replaces deleted values by Tombstones (None)
    """
    raise NotImplementedError("Implement this function")

def hash_quadratic(d):
    """Inserts/deletes keys from the list d into a hash table
    and returns the HashTable which contains the state of the 
    hash table after these insertions. Positive values in d
    are insertions, negative values deletions.

    Use just one HashTable instance inside this function.
    
    Uses quadratic probing to resolve collisions.

    Replaces deleted values by Tombstones (None)
    """
    raise NotImplementedError("Implement this function")