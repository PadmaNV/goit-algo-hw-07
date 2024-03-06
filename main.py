class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


"""ЗАВДАННЯ 1. Напишіть алгоритм (функцію), який знаходить найбільше значення
 у двійковому дереві пошуку"""
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val

"""Кінець завдання 1."""


"""ЗАВДАННЯ 2. Напишіть алгоритм (функцію), який знаходить найменше значення 
у двійковому дереві пошуку"""
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val

"""Кінець завдання 2."""


"""ЗАВДАННЯ 3. Напишіть алгоритм (функцію), який знаходить суму всіх значень
 у двійковому дереві пошуку"""
def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

"""Кінець завдання 3."""

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# root = delete(root, 7)

min_value = min_value_node(root)
print("ЗАВДАННЯ 1:", "\n" , "Мінімальне значення в дереві:", min_value, "\n")

max_value = max_value_node(root)
print("ЗАВДАННЯ 2:", "\n" , "Максимальне значення в дереві:", max_value, "\n")

total_sum = tree_sum(root)
print("ЗАВДАННЯ 3:", "\n" , "Сума всіх значень в дереві:", total_sum, "\n")


print(root)