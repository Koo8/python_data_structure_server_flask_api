from binary_search_lesson2 import User, insert_node, update_node, find_node, make_balanced_bst_from_sorted_list

class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value): ## TODO: when this is called??????
        print("in __setitem__")
        node = find_node(self.root, key)
        if node:
            tree = update_node(self.root, key, value)
            make_balanced_bst_from_sorted_list(tree)
        else:
            insert_node(self.root, key, value)

    def __getitem__(self, key):
        print('__in_getitem__')
        node = find_node(self.root, key)
        if node:
            return node.value
        else:
            return None


treemap = TreeMap()
print(treemap.root),
treemap.__setitem__('nancy', User('nancy', 'nancy', 'nancy@gmail.com'))
print(treemap.root) ##????