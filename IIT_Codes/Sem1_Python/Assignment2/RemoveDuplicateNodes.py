
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def removeDuplicates(head):
    if head is None:
        return head

    current = head
    prev = head

    while current is not None:
        if current.data == prev.data:
            prev.next = current.next
        else:
            prev = current

        current = current.next

    return head




def printSinglyLinkedList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


def swap(ptr1, ptr2):
    tmp = ptr2.data
    ptr2.data = ptr1.data
    ptr1.data = tmp


def bubbleSort(head):
    swapped = True

    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.data > current.next.data:
                swap(current, current.next)
                swapped = True
            current = current.next


n = int(input())
m = int(input())

head = None
tail = None

for _ in range(m):
    data = int(input())
    if head is None:
        head = Node(data)
        tail = head
    else:
        tail.next = Node(data)
        tail = tail.next

bubbleSort(head)
revised = removeDuplicates(head)
printSinglyLinkedList(head)