class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head  # nodeA
        while temp:
            print(temp.data)
            temp = temp.next

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):

        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def after_node_add(self, prev_node, new_data):
        if not prev_node:
            print("No previous node found")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None


nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')

llist = LinkedList()
llist.head = nodeA
nodeA.next = nodeB

# llist.head.next = nodeB
nodeB.next = nodeC
# print(llist.print_list())
# print(nodeB.next.data)
# llist.add_last('D')
llist.after_node_add(nodeB, 'D')
print(llist.print_list())
