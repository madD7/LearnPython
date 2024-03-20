import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def insertNodeAtHead(self, data):
        temp = self.head
        self.head = SinglyLinkedListNode(data)
        self.head.next = temp


def insertNodeAtHead(llist, data):
    temp = llist
    llist = SinglyLinkedListNode(data)
    llist.next = temp
    return llist

def insertNodeAtPosition(llist, data, position):
    prev = llist
    nxt = llist

    for i in range(position):
        prev = nxt
        nxt = nxt.next

    node = SinglyLinkedListNode(data)
    prev.next = node
    node.next = nxt

    return llist

def reverseList(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data), end='')
        node = node.next

        if node:
            print(sep)

def deleteDuplicateNodes(head):
    temp = head
    while temp:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head

def CheckIfPalindrome(head):
    temp = head
    stack = []

    while temp:
        stack.append(str(temp.data))
        temp = temp.next

    return stack == stack[::-1], stack[(len(stack)//2)], max(stack)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())
    llist = SinglyLinkedList()

    if 0 >= llist_count >= 10**5: #llist_count
        sys.exit(0)

    for _ in range(llist_count):
        llist_item = input()
        llist.insert_node(llist_item)

    # data = int(input())                       # Input Data
    # position = int(input())                   # Input Position
    # llist_head = insertNodeAtPosition(llist.head, data, position)
    # print_singly_linked_list(llist_head, ' ')
    llist_head = reverseList(llist.head)

    verify, mid, maxvalue = CheckIfPalindrome(llist_head)

    if verify:
        print("Yes")
        print(mid)
    else:
        print("No")
        print(maxvalue)

    # print_singly_linked_list(llist_head, ' ')