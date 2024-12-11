#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime n
    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers, where each integer n represents


    Returns:
        str: The name of the player who won the most rounds
    Raises:
        None.
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores and array of possible
    ben = 0
    maria = 0
    # Create a list 'a' of length sorted(nums)
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    # The first two elements of the list
    a[0], a[1] = 0, 0
    # Use Sieve of Eratosthenes
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Play each round of the game
    for i in nums:
        # If the sum of prime numbers in t
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removes multiples of a prime number

    This function iterates through
    Args:
        ls (list of int): A list of integers
        x (int): The prime number for

    Returns:
        None: This function modifies

    Raises:
        None.
    """
    # This loop iterates over multiples
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
