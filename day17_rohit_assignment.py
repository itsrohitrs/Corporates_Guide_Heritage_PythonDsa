# ==========================================
# DSA MODULE 3 ASSIGNMENT
# Linked Lists

# Question 1
# Node, Head, Pointer Explanation
# ==========================================

print("========== Question 1 ==========")

print("""
Node:
A node is the basic building block of a Linked List.
Each node contains:
1. Data
2. Pointer (Reference to next node)

Head:
The head is the first node of the linked list.
It is used to access the entire list.

Pointer:
A pointer (reference) stores the address of the next node.
It creates the chain between nodes.

Representation:

Head
 |
 v
[3|*] -> [16|*] -> [9|*] -> [21|None]

The last node points to None, indicating the end of the list.
""")


# ==========================================
# Node Class
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================
# Question 2
# Insert at End
# ==========================================

print("\n========== Question 2 ==========")

def insert_at_end(head, data):

    new_node = Node(data)

    # Empty list
    if head is None:
        return new_node

    current = head

    while current.next:
        current = current.next

    current.next = new_node

    return head


# Testing
head = None

head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
head = insert_at_end(head, 30)

print("Linked List after insertion:")

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")


# ==========================================
# Question 3
# Singly vs Doubly Linked List
# ==========================================

print("\n========== Question 3 ==========")

print("""
Singly Linked List:
- Each node stores:
    Data + Next Pointer
- Traversal possible only in forward direction.

Example:
10 -> 20 -> 30 -> None

Doubly Linked List:
- Each node stores:
    Previous Pointer + Data + Next Pointer
- Traversal possible in both forward and backward directions.

Example:
None <- 10 <-> 20 <-> 30 -> None

Why deletion is easier in Doubly Linked List?

Because every node has a previous pointer.
If we already have a reference to a node,
we can directly connect its previous node
to its next node without searching from the head.
""")


# ==========================================
# Question 4
# Time Complexity Table
# ==========================================

print("\n========== Question 4 ==========")

print("""
Operation               Array           Linked List

Access by index         O(1)            O(n)

Insert at beginning     O(n)            O(1)

Insert at end           O(1)*           O(n)

*For dynamic arrays like Python lists, append is usually O(1).

Justification:

Array Access:
Arrays store elements in contiguous memory locations.
So arr[i] can be accessed directly in O(1).

Linked List Access:
To reach the ith node, we must traverse node by node.
Hence O(n).
""")


# ==========================================
# Question 5
# Size Method
# ==========================================

print("\n========== Question 5 ==========")

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def size(self):

        count = 0

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example

ll = LinkedList()

ll.insert_at_end(5)
ll.insert_at_end(10)
ll.insert_at_end(15)
ll.insert_at_end(20)

print("Linked List:")
ll.display()

print("Size of Linked List:", ll.size())