class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def contains(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next
        return False

    def delete(self, data):
        node = self.head
        # prev_node = self.head
        if node is not None:
            if node.data == data:
                self.head = node.next
                node = None
                return
        while node is not None:
            if node.data == data:
                prev_node.next = node.next
                node = None
                return
            prev_node = node
            node = node.next

    def detect_loop(self):
        slow = self.head
        fast = self.head.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        fast = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        print("Loop Found At: ", fast.data)

    def print_list(self):
        temp = self.head
        list = ""
        while temp:
            # print(temp.data)
            list += "->" + str(temp.data)
            temp = temp.next
        print(list)

if __name__ == "__main__":
    l_list = LinkedList()
    l_list.append(6)
    l_list.prepend(7)
    l_list.prepend(1)
    l_list.append(4)
    l_list.insertAfter(l_list.head.next, 8)
    l_list.print_list()
    # print(l_list.contains(8))
    # l_list.delete(1)
    # print("=====================")
    # l_list.print_list()
    l_list.head.next.next.next = l_list.head.next
    l_list.detect_loop()
