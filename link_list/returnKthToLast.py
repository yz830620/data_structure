from linkedlist import LinkedList

ll = LinkedList()


def nth_to_last(li, n):
    pointer1 = li.head
    pointer2 = li.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()

customLL.generate(10, 0, 99)
print(customLL)
result = nth_to_last(customLL, 3)
print(result)