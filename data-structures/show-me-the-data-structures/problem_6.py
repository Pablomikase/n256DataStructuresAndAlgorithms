from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    firs_set = set()
    second_set = set()
    if llist_1.head is not None:
        node = llist_1.head
        while node:
            firs_set.add(node.value)
            node = node.next
    if llist_2.head is not None:
        node = llist_2.head
        while node:
            second_set.add(node.value)
            node = node.next

    result_set = set()
    #add all elements from first set to the result
    for element_first_set in firs_set:
        result_set.add(element_first_set)
    #add all elements from second set to the result
    for element_second_set in second_set:
        result_set.add(element_second_set)
    # Create a new linked list to store the union
    result = LinkedList()
    for element in result_set:
        result.append(element)
    return result


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    firs_set = set()
    second_set = set()
    if llist_1.head is not None:
        node = llist_1.head
        while node:
            firs_set.add(node.value)
            node = node.next
    if llist_2.head is not None:
        node = llist_2.head
        while node:
            second_set.add(node.value)
            node = node.next

    result = LinkedList()

    # Find the intersection of both sets
    for element_first_set in firs_set:
        for element_second_set in second_set:
            if element_first_set == element_second_set:
                result.append(element_first_set)

    return result

if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3 -  empty linked list Union
    print("Test Case 3:empty linked list Union")
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    print("Union:", union(linked_list_5, linked_list_6)) # Expected: empty

    ## Test case 4 -  empty linked list Intersection
    print("Test Case 3:empty linked list Intersection")
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    print("Intersection:", intersection(linked_list_5, linked_list_6))  # Expected: empty

    ## Test case 5 - Union one empty and other not
    print("Test Case 3:Union one empty and other not")
    linked_list_5 = LinkedList()
    element_2 = [1, 7, 8, 9, 11, 21, 1]
    for i in element_2:
        linked_list_5.append(i)
    linked_list_6 = LinkedList()
    print("Union:", union(linked_list_5, linked_list_6))

    #Test case 6 - Union and Intersection with same elements
    print("#Test case 6 - Union and Intersection with same elements")
    llist_1 = LinkedList()
    llist_2 = LinkedList()
    for i in [1, 2, 3]:
        llist_1.append(i)
        llist_2.append(i)
    print("Union:", union(llist_1, llist_2))  # Expected: 1, 2, 3
    print("Intersection", intersection(llist_1, llist_2))  # Expected: 1, 2, 3
