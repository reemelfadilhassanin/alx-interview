#!/usr/bin/python3
'''The minimum operations coding challenge.
This function calculates the minimum number of operations
to achieve exactly n 'H' characters using only Copy All
and Paste operations.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to reach n
    'H' characters, or 0 if n is impossible to achieve.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0  # Return 0 for invalid input (not a positive integer)

    ops_count = 0  # Initialize operation count
    clipboard = 0  # Initialize clipboard (no characters copied yet)
    done = 1       # Start with 1 character 'H'

    while done < n:
        if clipboard == 0:
            # First operation: Copy All (initially copy 'H')
            clipboard = done  # Set clipboard to current character count
            done += clipboard  # Paste it to the document
            ops_count += 2     # Count both Copy and Paste operations

        elif n - done > 0 and (n - done) % done == 0:
            # If remaining characters can be achieved by pasting current count
            clipboard = done  # Update clipboard to current character count
            done += clipboard  # Paste the characters
            ops_count += 2     # Count both Copy and Paste operations

        elif clipboard > 0:
            # Paste operation: add clipboard count to the current total
            done += clipboard  # Paste the copied characters
            ops_count += 1     # Count the Paste operation

    return ops_count  # Return the total number of operations
