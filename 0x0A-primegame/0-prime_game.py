#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Returns a list of primes up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    """Determines the winner of the prime game based on given rounds."""
    maria_wins = 0
    ben_wins = 0

    # For each round, determine who wins based on the number of primes
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        # If the number of primes is odd, Maria wins (since she starts first)
        if len(primes) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player with most wins, or None if it's a tie
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
