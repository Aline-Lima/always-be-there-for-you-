# Author: Aline Botti
# GitHub username: Aline_Lima
# Date: 02/15/2023
# Description: Function row_puzzle tries to achieve 0 value from puzzle line using recursion



def row_puzzle(puzzle, index, visited_List):
    """defines the function using puzzle, index, visited_List"""
    if puzzle[index] == 0:
        return True
    """ if it can't go left, this is a failure"""
    if index < 0:
        return False

    """if we can't go right, this is a failure"""
    if index >= len(puzzle):
        return False
    else:
        visited_List.append(index)

    """" recursive case: at least one path has to be true"""
    """ check to see if left or right gives a valid path"""
    return row_puzzle(puzzle, index-puzzle(index), visited_List) or row_puzzle(puzzle, index+puzzle(index), visited_List)

