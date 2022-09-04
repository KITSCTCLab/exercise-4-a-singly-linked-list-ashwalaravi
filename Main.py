from typing import Optional


class Node:
    """
    Provide necessary documentation
    """

    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """

    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):

        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Writ code here
        t = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while t.next is not None:
                t = t.next
            t.next = new_node

    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        b = []
        while self.head:
            b.append(self.head.data)
            self.head = self.head.next
        print(b)


class Solution:
    """
    Provide necessary documentation
    """

    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """

        # Write code here
        self.first_list = first_list
        self.second_list = second_list

        dummy = LinkedList()

        othervar = dummy
        carry = 0

        while first_list or second_list or carry:
            v1 = self.first_list.head.data if first_list else 0
            v2 = self.second_list.head.data if second_list else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            othervar.insert_at_end(val)



            first_list = self.first_list.head.next if first_list else None
            second_list = self.second_list.head.next if second_list else None
        return dummy





# Do not edit the following code
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
