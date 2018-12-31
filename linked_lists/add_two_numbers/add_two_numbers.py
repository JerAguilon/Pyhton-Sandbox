class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.x = x

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry_over = 0

        curr_l1 = l1
        curr_l2 = l2

        head = None
        tail = None

        while curr_l1 is not None and curr_l2 is not None:
            curr_digit_total = curr_l1.x + curr_l2.x + carry_over

            if curr_digit_total >= 10:
                carry_over = int(curr_digit_total / 10)
                curr_digit_total = curr_digit_total % 10
            else:
                carry_over = 0

            new_node = ListNode(curr_digit_total)
            if tail:
                tail.next = new_node
                tail = new_node
            else:
                head = new_node
                tail = new_node

            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next

        while curr_l1 is not None:
            curr_digit_total = curr_l1.x + carry_over
            if curr_digit_total >= 10:
                carry_over = int(curr_digit_total / 10)
                curr_digit_total = curr_digit_total % 10
            else:
                carry_over = 0
            new_node = ListNode(curr_digit_total)

            if tail:
                tail.next = new_node
                tail = new_node
            else:
                head = new_node
                tail = new_node
            curr_l1 = curr_l1.next

        while curr_l2 is not None:
            curr_digit_total = curr_l2.x + carry_over
            if curr_digit_total >= 10:
                carry_over = int(curr_digit_total / 10)
                curr_digit_total = curr_digit_total % 10
            else:
                carry_over = 0

            new_node = ListNode(curr_digit_total)
            if tail:
                tail.next = new_node
                tail = new_node
            else:
                head = new_node
                tail = new_node
            curr_l2 = curr_l2.next

        if carry_over != 0:
            tail.next = ListNode(carry_over)

        return head


def print_values(head):
    while head:
        print(head.x)
        head = head.next

def test():
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6

    result = Solution().addTwoNumbers(l1, l4)

    print_values(result)
    assert result.x == 7
    assert result.next.x == 0
    assert result.next.next.x == 8
    assert result.next.next.next == None

test()
