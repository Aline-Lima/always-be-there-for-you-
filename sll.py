# Name: Aline Lindholm Lima Botti
# Description: This is a Linked List


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel). It
must be implemented with O(1) runtime complexity.
        """

        new_head_node = SLNode(value, self._head)
        second_head_node = SLNode(value, self._head.next)
        new_head_node.next = self._head

        self._head.next = second_head_node



    def insert_back(self, value: object) -> None:
            """
            This method adds a new node at the end of the list. It must be implemented with O(N)
            runtime complexity.
            """

            last_node = SLNode(value)
            node = self._head
            while node.next:
                node = node.next
            node.next = last_node



    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”. Code for the
        exception is provided in the skeleton file. If the linked list contains N nodes (the sentinel
        node is not included in this count), valid indices for this method are [0, N] inclusive. It
        must be implemented with O(N) runtime complexity.
        """

        if index < 0 or index > self.length():
            raise SLLException("Exception")
        new_value = SLNode(value)
        node = self._head
        for i in range(index):
            node = node.next
        new_value.next = node.next
        node.next = new_value

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”. Code for the
        exception is provided in the skeleton file. If the list contains N elements (the sentinel node
        is not included in this count), valid indices for this method are [0, N - 1] inclusive. It must
        be implemented with O(N) runtime complexity
        """
        if index < 0 or index >= self.length():
            raise SLLException("Exception")
        node = self._head
        for i in range(index):
            node = node.next
        node.next = node.next.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end, and removes the first node
        that matches the provided “value” object. The method returns True if a node was removed
        from the list. Otherwise, it returns False. It must be implemented with O(N) runtime
        complexity.
        """

        first_node = self._head
        while first_node.next:
            if first_node.next.value == value:
                first_node.next = first_node.next.next
                return True
            first_node = first_node.next
        return False


    def count(self, value: object) -> int:
            """
            This method counts the number of elements in the list that match the provided “value”
            object. The method then returns this number. It must be implemented with O(N)
            runtime complexity.
            """

            n = 0
            node = self._head.next
            while node:
                if node.value == value:
                  n += 1
                node = node.next

            return n

    def find(self, value: object) -> bool:
            """
            This method returns a Boolean value based on whether or not the provided “value” object
            exists in the list. It must be implemented with O(N) runtime complexity.
            """
            node = self._head.next
            while node:
                if node.value == value:
                    return True
                node = node.next


            return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList object that contains the requested number of nodes
        from the original list, starting with the node located at the requested start index. If the
        original list contains N nodes, a valid start_index is in range [0, N - 1] inclusive. The
        original list cannot be modified. The runtime complexity of your implementation must
        be O(N).
        You are allowed to directly access the variable (_head) of LinkedList objects you create. If
        the provided start index is invalid, or if there are not enough nodes between the start index
        and the end of the list to make a slice of the requested size, this method raises a custom
        “SLLException”. Code for the exception is provided in the skeleton file.
        """
        if start_index < 0 or start_index >= self.length():
            raise SLLException(Exception)
        if size < 0 or start_index + size > self.length():
            raise SLLException(Exception)
        ll = LinkedList()
        node = self._head.next
        for i in range(start_index):
            node = node.next
        for i in range(size):
            ll.insert_back(node.value)
            node = node.next
        return ll


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
