#!/usr/bin/env python

#### WRITE YOUR SOLUTION BELOW####
#### COPY YOUR CODE FROM BELOW INTO A FILE q1.py FOR SUBMISSION ####
def compute_winner(history_A, history_B):
    """Computes the winner of the coin flipping game given the histories
    of players A and B.
    Returns "A" if player A wins, "B" if player B wins, and "D" if it is a draw.
    """
    raise NotImplementedError("Implement this function")

def encode(history):
    """Takes as input a string representing the history of a player and returns its
    compressed representation."""
    raise NotImplementedError("Implement this function")

def decode(compressed_history):
    """Takes as input a compressed representation of a player's history and returns
    an uncompressed representation of the same history."""
    raise NotImplementedError("Implement this function")

def compute_winner_compressed(compressed_history_A, compressed_history_B):
    """Computes the winner of a game given two compressed histories. Your implementation
    must not use your implementations of compute_winner, the encoder/decoder pair, or some other
    technique that is identical to decoding the compressed move sequences before computing
    the winner as before."""
    raise NotImplementedError("Implement this function")

#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q1.py ####

history_a = "HTHTTH"
history_b = "THTTHH"


def q1_simple_tests():
    assert(compute_winner(history_a,history_b)=="B")
    assert(encode(history_a)=="H1T1H1T2H1")
    assert(encode(history_b)=="T1H1T2H2")
    assert(decode("T1H1T2H2")=="THTTHH")
    assert(compute_winner_compressed(encode(history_a),encode(history_b))=="B")
    
