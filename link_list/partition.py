from linkedlist import LinkedList

def partition(li, x):
    curNode = li.head
    li.tail = li.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = li.head
            li.head = curNode
        else:
            li.tail.next=curNode
            li.tail = curNode
        curNode = nextNode
        
    if li.tail.next is not None:
        li.tail.next = None
    return li

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)

print(partition(customLL, 40))