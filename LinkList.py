class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        # make sure item is a proper node
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def show(self):
        self.show_s(self.head)

    def show_s(self, item):
        if item != None:
            print(item.val)
            self.show_s(item.next)

list1 = Linked_List()

node1 = Node(15)

list1.add_list_item(node1)
list1.add_list_item(6)
list1.add_list_item(7)
list1.add_list_item(7)
list1.add_list_item(12)

list1.show()