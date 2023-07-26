def pascal_triangle(n):
    """Returns a list of lists of intergers representing the Pascal's triangle of n"""
    lists = [ ]

    if n <= 0:
        lists = [[]]
        return lists
    for i in range(n):
        lists_item = [1]
        for j in range(i):
            if j == i - 1:
                lists_item.append(1)
            else:
                item = lists[-1][j] + lists[-1][(j + 1)]
                lists_item.append(item)
        lists.append(lists_item)
    return lists
