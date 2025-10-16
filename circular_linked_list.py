from node import Node

class CircularLinkedList:
    
    def __init__(self):
       
        self.head = None
    
    def insert_end(self, data):
      
        new_node = Node(data)
        
        if self.head is None:
           
            self.head = new_node
            new_node.next = self.head
        else:
            
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
    
    def insert_begin(self, data):
     
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node
    
    def insert_after(self, target, data):
    
        if self.head is None:
            print(f"List is empty. Cannot insert after {target}")
            return
        
        current = self.head
        found = False

        while True:
            if current.data == target:
                found = True
                break
            current = current.next
            if current == self.head:
                break
        
        if found:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        else:
            print(f"Node with value {target} not found")
    
    def delete_node(self, key):
        
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        prev = None

        if current.data == key:

            if current.next == self.head:
                self.head = None
                return

            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
        
        print(f"Node with value {key} not found")
    
    def search(self, key):
     
        if self.head is None:
            return False
        
        current = self.head
        
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        
        return False
    
    def reverse(self):
       
        if self.head is None or self.head.next == self.head:
            return
        
        prev = None
        current = self.head
        next_node = None
        tail = self.head
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            if current == self.head:
                break

        self.head.next = prev
        self.head = prev
    
    def display(self):

        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        result = []
        
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(result) + " -> (back to head)")
    
    def count_nodes(self):
        
        if self.head is None:
            return 0
        
        count = 1
        current = self.head.next
        
        while current != self.head:
            count += 1
            current = current.next
        
        return count
    
    def clear(self):
        self.head = None
