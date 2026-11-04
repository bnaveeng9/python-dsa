from python_dsa.utils.linkedList import LinkedList  


def test_add_node_Delete_node():
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

def test_acyclic_linkedlist():
    ll: LinkedList = LinkedList()

    # Add nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)
    ll.add_node(60)

    print("Initial List:", ll.display())  

    ll.add_node(70)
    ll.create_cycle_in_linkedlist(30)
    print(f"is cycle in the linkedlist: {ll.has_cycle()}")
    print("after creatign a loop the List:", ll.display_cyclic_linkedlist())
    #print("after creatign a loop the List:", ll.display())  

if __name__ == "__main__":
    test_acyclic_linkedlist()