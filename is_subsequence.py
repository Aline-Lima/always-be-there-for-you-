# Author: Aline Botti
# GitHub username: Aline_Lima
# Date: 02/14/2023
# Description: takes two string parameters and returns True if the first string is a subsequence of the second string, but returns False otherwise.

def is_subsequence(first, second):
    """
    Returns a new string that is the reverse of st
    """
    """base case 1"""
    if len(first) == 0:
        return True
    """base case 2"""
    if len(second) == 0:
        return False

    if first[0] == second[0]:
      return is_subsequence(first[1:], second[1:])
    else:
      return is_subsequence(first, second[1:])


def main():
  print(is_subsequence("banana","apple"))
