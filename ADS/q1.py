def compute_winner(history_A, history_B):
    """Computes the winner of the coin flipping game given the histories
    of players A and B.
    Returns "A" if player A wins, "B" if player B wins, and "D" if it is a draw.
    """
    # PLAN
    #   once we have enough history - check the last 4 results of each player
    #   if that window is HTTH - note the turn they got it on, compare with the other player
    #   otherwise - remove the first value, add the new one. i.e. slide the window forwards

    # find outcome of player A
    counterA = 1
    window_A = ""
    winning_sequence = "HTTH"
    for turn in history_A:
        if len(window_A) < 4:
            window_A += turn
            counter += 1
        else:
            if window_A == winning_sequence:
                break
            else:
                window_A += turn 
                window_A = window_A[1:]

    # find outcome of player B
    counterB = 1
    window_B = ""
    for turn in history_A:
        if len(window_B) < 4:
            window_B += turn
            counter += 1
        else:
            if window_B == winning_sequence:
                break
            else:
                window_B += turn 
                window_B = window_B[1:]

                counter += 1

    if counterA == counterB:
        return "D"
    elif counterA < counterB:
        return "A"
    elif counterB < counterA:
        return "B"

    # only using for loops gives time complexity O(n)
    # this version also works for n of different sizes - if we assume n is same for both, we can use one for loop

def encode(history):
    """Takes as input a string representing the history of a player and returns its
    compressed representation."""
    compressed_history = ""
    compressed_history += history[0] # this makes the loop simpler
    cuurent_count = 1
    for i in len(history):           # we want to compare current and previous elemnts, so indexing is better
        if history[i] == history[i-1]:
            current_count += 1
        else:
            if current_count == 1:
                compressed_history += history[i]
                current_count = 1
            else:
                compressed_history += history[i-1]
                compressed_history += str(current_count)
                compressed_history += history[i]
                current_count = 1

    return compressed_history

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