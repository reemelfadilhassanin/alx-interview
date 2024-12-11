#!/usr/bin/python3
"""Module defines the isWinner"""

def isWinner(x, nums):
    """Function to determine who has won."""
    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        rounds_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        if not primes_set:
            ben_wins_count += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)

            # Remove multiples of the smallest prime
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            # Toggle turns
            is_maria_turn = not is_maria_turn

    if maria_wins_count > ben_wins_count:
        return "Winner: Maria"

    if maria_wins_count < ben_wins_count:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is a prime number, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers"""
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes
