# LINKED LIST IMPLEMENTATION

class LinkedList:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}{self.next}"    
    
 
a  = LinkedList(245,"no")

