from circular_linked_list import CircularLinkedList

def main():

    cll = CircularLinkedList()
    
    print("=" * 50)
    print("Circular Linked List Operations Demo")
    print("=" * 50)
    

    print("\n1. Inserting nodes at the end: 5, 10, 20, 25, 30")
    cll.insert_end(5)
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(25)
    cll.insert_end(30)
    
    print("\nCircular Linked List:")
    cll.display()

    print("\n2. Inserting 3 at the beginning")
    cll.insert_begin(3)
    cll.display()

    print("\n3. Inserting 15 after 10")
    cll.insert_after(10, 15)
    cll.display()

    print("\n" + "=" * 50)
    print("Resetting to original list for demo...")
    print("=" * 50)
    cll.clear()
    cll.insert_end(5)
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(25)
    cll.insert_end(30)
    
    print("\nCircular Linked List:")
    cll.display()

    print("\n4. Deleting node with value 10...")
    cll.delete_node(10)
    cll.display()
    
    print("\n5. Testing search operation:")
    print(f"Searching for 25: {cll.search(25)}")
    print(f"Searching for 100: {cll.search(100)}")
    

    print("\n6. Reversing the list...")
    cll.reverse()
    cll.display()

    print(f"\n7. Total nodes: {cll.count_nodes()}")

    print("\n8. Clearing the list...")
    cll.clear()
    cll.display()
    
    print("\n" + "=" * 50)
    print("All operations completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
