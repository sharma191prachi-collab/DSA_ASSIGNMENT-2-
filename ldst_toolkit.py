
     #1.DYNAMIC ARRAY
     
class DynamicArray:
    def __init__(self):
        self.capacity = 2   # starting capacity
        self.size = 0       # number of elements
        self.arr = [None] * self.capacity

    #  Append function
    def append(self, x):
        # agar array full hai → resize
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1

    #  Resize function (double capacity)
    def resize(self):
        print("Resizing from", self.capacity, "to", self.capacity * 2)

        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity

        # copy old elements
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    # Pop function
    def pop(self):
        if self.size == 0:
            print("Array is empty!")
            return None

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return value

    # Print function
    def print_array(self):
        print("Array:", end=" ")
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print("\nSize:", self.size, "Capacity:", self.capacity)


# Testing
da = DynamicArray()

# append elements
for i in range(1, 11):
    da.append(i)
    da.print_array()

# pop 3 elements
print("\nPopping elements:")
print("Removed:", da.pop())
print("Removed:", da.pop())
print("Removed:", da.pop())

da.print_array()


# 2.LINKED list
# (A)SINGLY LINKED LIST

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    #  Insert at beginning
    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    #  Insert at end
    def insert_at_end(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete by value
    def delete_by_value(self, x):
        temp = self.head

        # if we wan to delete first node
        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    # Traverse (print)
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Testing
sll = SinglyLinkedList()

# insert at beginning
sll.insert_at_beginning(3)
sll.insert_at_beginning(2)
sll.insert_at_beginning(1)
sll.traverse()

# insert at end
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.traverse()

# delete by value
sll.delete_by_value(3)
sll.traverse()

    #(B)DOUBLY LINKED LIST
    
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #  Insert after a given value
    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    #  Delete at position (0-based index)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # delete head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # move to position
        for i in range(pos):
            temp = temp.next
            if temp is None:
                print("Position out of range")
                return

        # delete node
        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # Traverse (print)
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Testing
dll = DoublyLinkedList()

# manually adding initial nodes
dll.head = Node(1)
n2 = Node(2)
n3 = Node(3)

dll.head.next = n2
n2.prev = dll.head
n2.next = n3
n3.prev = n2

dll.traverse()

# insert after value
dll.insert_after(2, 5)
dll.traverse()

# delete at position
dll.delete_at_position(1)
dll.traverse()


     #3.STACK AND QUEUE
     
    # A.STACK
    # Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class
class Stack:
    def __init__(self):
        self.top = None   # head of linked list

    # Push (add element)
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    #  Pop (remove element)
    def pop(self):
        if self.top is None:
            print("Stack is empty!")
            return None

        value = self.top.data
        self.top = self.top.next
        return value

    # Peek (top element dekhna)
    def peek(self):
        if self.top is None:
            print("Stack is empty!")
            return None

        return self.top.data

    # Print stack
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Testing
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:")
s.display()

print("Top element:", s.peek())

print("Removed:", s.pop())
s.display()
    
    
    # B.QUEUE
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear = None

    # enqueue (add)
    def enqueue(self, x):
        new = Node(x)

        if self.rear is None:
            self.front_node = new
            self.rear = new
            return

        self.rear.next = new
        self.rear = new

    # dequeue (remove)
    def dequeue(self):
        if self.front_node is None:
            return "Queue empty"

        val = self.front_node.data
        self.front_node = self.front_node.next

        if self.front_node is None:
            self.rear = None

        return val

    # front (first element)
    def front(self):
        if self.front_node is None:
            return "Queue empty"
        
        return self.front_node.data

    # print
    def show(self):
        temp = self.front_node
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# testing
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.show()           
print(q.front())  
print(q.dequeue()) 
q.show()           



      #3.PARENTHESES CHECKER
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expr):
    s = Stack()

    for ch in expr:
        # opening brackets
        if ch in "({[":
            s.push(ch)

        # closing brackets
        elif ch in ")}]":
            if s.is_empty():
                return False

            top = s.pop()

            if (ch == ")" and top != "(") or \
               (ch == "}" and top != "{") or \
               (ch == "]" and top != "["):
                return False

    return s.is_empty()


#  Testing
print(is_balanced("([])"))   # True
print(is_balanced("([)]"))   # False
print(is_balanced("((("))    # False
print(is_balanced(""))       # True