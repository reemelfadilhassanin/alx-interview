#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    n = len(boxes)
    visited = [False] * n  # Track visited boxes
    visited[0] = True  # The first box is unlocked
    stack = [0]  # Start from the first box

    while stack:
        current_box = stack.pop()
        
        for key in boxes[current_box]:
            if key < n and not visited[key]:  # Check if the key is valid and box is not visited
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add to stack for further exploration

    return all(visited)  # Check if all boxes have been visited
