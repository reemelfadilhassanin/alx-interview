def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    
    If n <= 0, return an empty list.
    """
    if n <= 0:
        return []
    
    tra = [[1]]  # Start with the first row

    for i in range(1, n):
        temp = [1]  # Each row starts with a 1
        for j in range(len(tra[i - 1]) - 1):
            temp.append(tra[i - 1][j] + tra[i - 1][j + 1])
        temp.append(1)  # Each row ends with a 1
        tra.append(temp)

    return tra
	