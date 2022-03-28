class Node:
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self,key, value):
        self.key = key
        self.value = value

class HashedTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.ht =[None] * self.table_size

    def create_hash(self, key):
        hashed_key = 0
        for i in key:
            hashed_key += ord(i)
            hashed_key = (ord(i)* hashed_key) % self.table_size

        return hashed_key

    def add_key_value_to_ht(self,key,value):
        # hash the key - turn it to the ht index
        hashed_key = self.create_hash(key)
        print(f'hashed_key for {key} is {hashed_key}')
        if self.ht[hashed_key] is None: # this hased_key is still empty
            self.ht[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.ht[hashed_key]
            while node.next_node:
                node = node.next_node
            # loop till reach the last node under this hashed_key index
            node.next_node = Node(Data(key, value), None)

    def get_value_from_key(self,key):
        #get hashed_key
        hashed_key = self.create_hash(key)
        if self.ht[hashed_key] is not None:
            node = self.ht[hashed_key]
            # if only one node
            if node.next_node  is None:
                return node.data.value
            while node.next_node:
                # if found the matching key during the loop
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            # check if the last node has the key
            if key == node.data.key:
                return node.data.value
        return None

    def print_table(self):
        print('{')
        for i, val in enumerate(self.ht):
            if val is not None:
                list_str = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        list_str += f'{node.data.key} : {node.data.value} -->  '
                        node = node.next_node
                    list_str += f'{node.data.key} : {node.data.value} --> None'
                    # print(f'[{i}] : {list_str}')
                else:
                    list_str += f'{node.data.key} : {node.data.value}'
                print(f'[{i}] : {list_str}')

            else:
                print(f'[{i}] : {val}')

        print('}')
#
# ht = HashedTable(10)
# ht.add_key_value_to_ht('title','how to make money online')
# ht.add_key_value_to_ht('body','this is the long part of the article, it takes 3 paragraphs.')
# ht.add_key_value_to_ht('date', 'today')
# ht.add_key_value_to_ht('id', '12')
# ht.print_table()
# title = ht.get_value_from_key('title')
# date = ht.get_value_from_key('date')
# print(title)
# print(date)
#
