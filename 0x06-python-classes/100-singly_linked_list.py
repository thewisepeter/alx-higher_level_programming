#!/usr/bin/python3
"""singly linked list implementation"""


class Node:
    """node in a linked list"""

    def __init__(self, data, next_node=None):
        """initializes node"""

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """gets data"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets data"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """gets next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list"""

    def __init__(self):
        """initializes singly linked list"""

        self.__head = None

    def __str__(self):
        """makes list printable"""

        elements = ""
        current = self.__head
        while current:
            elements += str(current.data) + "\n"
            current = current.next_node
        return elements[:-1]

    def sorted_insert(self, value):
        """inserts node"""

        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        if current.next_node:
            new_node.next_node = current.next_node
        current.next_node = new_node
