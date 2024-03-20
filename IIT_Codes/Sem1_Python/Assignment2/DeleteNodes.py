import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def deleteNodes(head, n, m):
    current = head
    prev = head

    for _ in range(m):
        if current is None:
            return head

        prev = current
        current = current.next

    for _ in range(n):
        if current is None:
            break

        next = current.next
        current.next = None
        current = next

    prev.next = current

if __name__ == "__main__":
    n, x, y = map(int, input().split(','))

    if 1 >= n or n >= 100:
        sys.exit()

    if n <= x and (x <= 1 or x >= 100):
        sys.exit()

    if n <= y and (y <= 1 or y >= 100):
        sys.exit()

    head = None
    tail = None

    for _ in range(n):
        data = input()
        if head is None:
            head = Node(data)
            tail = head
        else:
            tail.next = Node(data)
            tail = tail.next

    deleteNodes(head, x, y)

    while head:
        print(head.data, end=' ')
        head = head.next