"""
    utils.py - contains some common helper funcs
"""


# HACK: appending this path in sys.path to avoid "ModuleNotFoundError"
#       while executing vim buffer
import sys
import pathlib
sys.path.append(pathlib.Path().absolute())


# importing standard modules to avoid re-importing them individually
from typing import List
from collections import defaultdict, Counter


# Leetcode's Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Leetcode's Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# build tree from level order traversal as array
def buildTree(nums: List[int], i: int = 0) -> TreeNode:

    if i >= len(nums):
        return

    root = TreeNode(nums[i])

    root.left = buildTree(nums, 2*i+1)
    root.right = buildTree(nums, 2*i+2)

    return root


# generate linked list from array (to avoid .next, .next.next manual calls)
def generateLL(nums: List[int]) -> ListNode:

    if not nums:
        return

    ll = tmp = ListNode(0)

    for num in nums:
        tmp.next = ListNode(num)
        tmp = tmp.next

    tmp.next = None

    return ll.next


# print linked list (useful for debugging)
def printLL(ll: ListNode):

    tmp = ll    # to avoid modifying original list
    while tmp:
        print(tmp.val, end="->")
        tmp = tmp.next

    print("")


