class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


n1 = Node(5)
n2 = Node(15)
n3 = Node(7)

n1.next = n2
n2.next = n3
# print(n1.next.next)
# print(n3)
# print(n1.next.next.val)
# print(n3.val)
print(n1.next.next.next)
