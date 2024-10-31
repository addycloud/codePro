#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not (0 <= data <= 9):
            raise ValueError("数据必须是一位数字。")
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("NULL")

# 创建链表并插入数据
linked_list = LinkedList()
linked_list.insert(5)
linked_list.insert(3)
linked_list.insert(8)
linked_list.display()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 通过循环读取l1每个数字，利用字符串将每个数字叠加成完整的数字
        num1 = str(l1.val)
        flag = l1.next
        while flag != None:
            num1 = str(flag.val) + num1
            flag = flag.next
        # 通过循环读取l2每个数字，利用字符串将每个数字叠加成完整的数字
        num2 = str(l2.val)
        flag = l2.next
        while flag != None:
            num2 = str(flag.val) + num2
            flag = flag.next
        # 转成int，进行求和，再转成字符串
        numSum = str( int(num1) + int(num2) )
        # 利用循环，逐个读取字符串并存储起来
        result = ListNode(val=int(numSum[0]))
        for i in range(len(numSum)-1):
            result = ListNode(val=int(numSum[i+1]), next=result)

        return result
