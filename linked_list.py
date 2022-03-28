class Node():
    def __init__(self, data:str=None, next_node=None):
        self.data = data # if append ',' comma at the end, the print method will show tuple instead of string of data
        self.next_node = next_node

class LinkedList():
    def __init__(self):
        self.head = None # if append "," a comma, this self.head will turn to be a tuple object, not a Node, which is wrong
        self.last_node = None

    def print_linkedlist(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f'{str(node.data)}  -> '
            node = node.next_node
        ll_string += 'None'
        print(ll_string)

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        if self.last_node is None:
            self.last_node = node

    def insert_at_end(self, data):
        node=Node(data,None)
        if self.last_node is None:
            self.last_node = node
            if self.head is None:
                self.head = node
        else:
            self.last_node.next_node = node
            self.last_node = node

    def to_list(self):
        l = []
        node = self.head
        if node is None:
            return l
        while node:
            l.append(node.data)
            node = node.next_node
        # print(l)
        return l

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] == int(user_id):
                return node.data
            node=node.next_node
        return None



