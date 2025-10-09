"""
RPS.py - Rock Paper Scissors Player Strategy

This module defines a function `player` that predicts the opponent's next move
based on the last 5 moves observed. It uses a weighted probability approach
and a small random factor to avoid predictable patterns.

Features:
- Tracks the last 5 opponent moves
- Predicts the opponent's next move using move frequency
- Plays the winning move against the predicted opponent move
- Adds a small random chance to break patterns (10%)
"""

import random
from collections import deque, Counter

# Possible moves
moves = ['R', 'P', 'S']

# Counter moves to win: Rock->Paper, Paper->Scissors, Scissors->Rock
counter = {'R': 'P', 'P': 'S', 'S': 'R'}

# Keep last 5 opponent moves
history = deque(maxlen=5)

def player(opponent_last_move):
    """
    Decide the next move based on opponent's last moves.

    Args:
        opponent_last_move (str or None): Opponent's previous move ('R','P','S') or None

    Returns:
        str: Player's next move ('R','P','S')
    """
    if opponent_last_move:
        # Record opponent's last move
        history.append(opponent_last_move)
    
    if history:
        # Count occurrences of each move in recent history
        counts = Counter(history)
        total = sum(counts.values())
        # Convert counts to weighted probabilities
        probs = {m: counts[m]/total for m in moves}
        # Predict opponent's next move based on weighted frequency
        predicted = random.choices(list(probs.keys()), weights=probs.values())[0]
        # Play the counter move
        move = counter[predicted]
    else:
        # If no history yet, pick a random move
        move = random.choice(moves)
    
    # Small random chance to break patterns
    if random.random() < 0.1:
        move = random.choice(moves)
    
    return move
