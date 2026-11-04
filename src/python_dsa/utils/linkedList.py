from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next : Optional[Node] = None

class LinkedList:
    """ single node in a linked list"""
    def __init__(self):
        # Initialize an empty list with no head
        self.head : Optional[Node] = None
        
    def add_node(self, data) -> None:
        new_node = Node(data)
        # if head is none or its a net new first node
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    """
    This will create a cyclic linked list. It goes to the end and connect the end node to 
    the existing node in the linked list
    """
    def create_cyclic_node(self, data) -> None:
            node_to_cycle = Node(data)
    
            # if head is none or its a net new first node
            if not self.head:
                self.head = node_to_cycle
                return 
            current = self.head
            while current.next:
                if current.data == data:
                    node_to_cycle = current
                current = current.next
            current.next = node_to_cycle

    def delete_node(self, data: int) -> bool:
        """Deletes the first node found containing target_value. Returns True if deleted."""
        # Case 1: List is empty
        if not self.head:
            return False

        current = self.head
        
        if current.data == data:
            #get next node if this head and reassign next to head

            if self.head.next:
                head_next = self.head.next
                self.head = head_next
                return True
            return False

        while current.next:
            if current.next.data == data:
                delete_node = current.next
                temp_next_next = delete_node.next
                current.next = temp_next_next
                return True
        return False

    """
    This function adds a last node to a node so that
    it will create a loop within a linked list.
    The purpose of this function to test Cycle detection program
    """
    def create_cycle_in_linkedlist(self, data: int) -> bool:
        if not self.head:
            return False

        current = self.head

        target_node = self.find_node(data)

        if target_node is None:
            return False
        while current.next:
            current = current.next
        current.next= target_node

    def find_node(self, data:int) -> Node | None:
        if not self.head:
            return None

        current = self.head

        while current.next:
          if current.data == data:
            return current
          current = current.next
        return None

    def has_cycle(self) -> bool:
        if self.head is None:
            return False

        if self.head.next is None or self.head.next.next is None:
            return False
        #print("step:1")
        current = self.head
        
        tortoise = self.head
        hare = tortoise.next.next
        #print("step:1.1")
        if hare is None or hare.next is None:
            return False
        
       # print("step:2")
        index = 2
        while (hare != tortoise ) and ( (hare.next is not None) ):
            index +=1
           # print(f"step:{index}")
            tortoise = tortoise.next
            hare = hare.next.next
            if hare is None or hare.next is None:
                return False
        return hare.next is not None








    def display(self) -> list[int]:
        """Helper to convert the linked list items to a standard Python list for visualization."""
        elements: list[int] = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    
    def display_cyclic_linkedlist(self) -> list[int]:
        """Helper to convert the linked list items to a standard Python list for visualization."""
        elements: list[int] = []
        current = self.head
        if not self.has_cycle():
            while current:
                elements.append(current.data)
                current = current.next
        else: 
            set_object = set()
            while current:
                elements.append(current.data)
                set_object.add(current.data)
                current = current.next
                if current.data in set_object:
                    print("In set the list is:", elements)
                    return elements
                        
        return elements

def main_():
    ll: LinkedList = LinkedList()

    # Add nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    print("Initial List:", ll.display())  # Output: [10, 20, 30]

    # Delete a middle node
    ll.delete_node(20)
    print("After deleting 20:", ll.display())  # Output: [10, 30]

    # Delete the head node
    ll.delete_node(10)
    print("After deleting head (10):", ll.display())  # Output: [30]


if __name__ == "__main__":
    main_()