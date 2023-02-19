# Author: Aline Lindholm Lima Botti
# GitHub username: Aline-Lima
# Date: 01/31/2023
# Description: modify insertion_sort to string_sort

def string_sort(a_list):
    """sort components of a list"""
    a_list_case = []
    for item in a_list:
        a_list_case.append(item.casefold())

    for index in range(1, len(a_list_case)):
        value = a_list_case[index]
        pos = index - 1
        while pos >= 0 and value < a_list_case[pos]:
            a_list_case[pos + 1] = a_list_case[pos]
            pos -= 1

        a_list_case[pos + 1] = value

    print(a_list_case)


def main():
    string_sort(["b", "a", "apple", "anKle"])


main()