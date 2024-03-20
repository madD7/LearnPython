class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, node_data):
        node = Node(node_data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

def print_singly_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next

def reverseLinkedList(head):
    if not head or not head.next:
        return head

    reversed_head = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

if __name__ == "__main__":
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = input().split(' ')
        llist_item = ''.join(llist_item)
        llist.insert_node(llist_item)

    llist1 = reverseLinkedList(llist.head)

    print_singly_linked_list(llist1)