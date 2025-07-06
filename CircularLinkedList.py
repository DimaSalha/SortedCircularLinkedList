class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        # 1 
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head
        prev = None

        # 2
        if value < self.head.data:
            # للوصول لآخر عنصر
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        # 3
        current = self.head
        while current.next != self.head and current.next.data < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        result = []
        current = self.head
        while True:
            result.append(f"[{current.data}]")
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(result))



scll = SortedCircularLinkedList()
for num in [7, 3, 9, 1, 4]:
    scll.insert(num)
    scll.print_list()
