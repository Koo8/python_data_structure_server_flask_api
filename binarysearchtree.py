class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_node_recursive(self, top_node, data):
        if top_node.data['id'] < data['id']:
            # check right node
            if top_node.right is None:
                top_node.right = Node(data)
            else:
                self._insert_node_recursive(top_node.right, data)
        elif top_node.data['id'] > data['id']:
            # check left node
            if top_node.left is None:
                top_node.left = Node(data)
            else:
                self._insert_node_recursive(top_node.left, data)
        else: # when the data is the same as the top_node.data, no insertion can happen, bst does not allow duplicate
            return

    def insert_node(self, data):
        if self.root is None: # an empty bst
            self.root = Node(data)
        else:
            #compare node value with root left node and right node
            self._insert_node_recursive(self.root, data)

    def _search_recursive(self, id, node):
        if id == node.data['id']:
            return node.data
        elif id < node.data['id'] and node.left is not None:
            return self._search_recursive(id, node.left)
        elif id > node.data['id'] and node.right is not None:
            return self._search_recursive(id, node.right)
        else:
            return False


    def search(self, id):
        the_id = int(id)
        if self.root is None:
            return False
        else:
            return self._search_recursive(the_id, self.root)




bst = BinarySearchTree()
bst.insert_node({'id': 15})
bst.insert_node({'id': 10})
bst.insert_node({'id': 2})
bst.insert_node({'id': 17})
bst.insert_node({'id': 33})