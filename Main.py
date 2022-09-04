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
        new_node = ListNode(data) 
        if self.head = new_node:
            return 
        t = self.head
        while(t.next):
            t = t.next
            
        t.next = new_node

            
        
    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        while (self.head ! = None):
            print(self.data)
            self.head = self.head.next
            
        
        
        
        


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        
        # Write code here
        dummy  = ListNode()
        othervar = dummy
        carry = 0
        while first_list or second_list or carry:
            v1 = first_list.data if first_list else 0
            v2 = second_list.data if second_list else 0
            
            val = v1 + v2 +carry 
            carry = val//10
            val = val %10
            othervar.next = ListNode(val)
            
            othervar = othervar.next
            first_list = first_list.next if first_list else None 
            second_list = second_list.next if second_list else None
        return dummy.next
            
        
        

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
