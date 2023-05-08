class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(linkedList):
    fastNode = linkedList
    slowNode = linkedList
    while fastNode is not None and fastNode.next is not None:
        fastNode = fastNode.next.next
        slowNode = slowNode.next
    return slowNode