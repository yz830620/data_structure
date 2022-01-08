from linkedlist import LinkedList


def sum_list(li1, li2):
    cur_li1 = li1.head
    cur_li2 = li2.head

    accu = 0
    result_list = LinkedList()

    while cur_li1 or cur_li2:
        print('ele in l1: ', cur_li1)
        print('ele in l2: ', cur_li2)
        if not cur_li1:
            cur_li1.value = 0
        if not cur_li2:
            cur_li2.value = 0
        next_digit = cur_li1.value + cur_li2.value + accu
        if next_digit >= 10:
            accu = 1
            next_digit -= 10
        else:
            accu = 0
        result_list.add(next_digit)
        cur_li1 = cur_li1.next
        cur_li2 = cur_li2.next
        print(result_list)
    return result_list


def sum_list_tur(l1, l2):
    n1 = l1.head
    n2 = l2.head
    
    carry = 0
    li = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        li.add(int(result % 10))
        carry = result // 10
    return li



li1 = LinkedList()
li2 = LinkedList()

li1.generate(3, 0, 9)
li2.generate(3, 0, 9)

print(sum_list_tur(li1, li2))

    