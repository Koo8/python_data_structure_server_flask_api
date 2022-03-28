class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @staticmethod
    def convert_tuple_to_bt(data): #((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
        # this tuple has 3 elements in the format of (leftSubtree, root, rightSubtree)
        if data is None:
            return None
        elif isinstance(data,tuple) and len(data)==3:
            node = TreeNode(data[1])
            node.left = TreeNode.convert_tuple_to_bt(data[0])
            node.right = TreeNode.convert_tuple_to_bt(data[2])
        else:
            node = TreeNode(data)
        return node

    def to_tuple(self): #((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
        # reverse the enginnering of the above method
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        # NOTE: use TreeNode.to_tuple() because this is a class method, not just a function outside of a class
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def display_keys(self, space='\t'*2, level=0):
        if self is None:
            print(level * space + '0')
            return
        if self.left is None and self.right is None:
            print((level) *space + str(self.key))
            return
        # NOTE: TreeNode.display_keys, not self.display_keys(), the latter will not allow level+1 argument to appear
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level+ str(self.key))
        TreeNode.display_keys(self.left, space, level+1)

    def traverse_inorder(self):
        # print(left_sub->root->right_sub)
        if self is None:
            return []
        # The + sign is used to perform the concatenation of two lists into one list with combined elements
        return (TreeNode.traverse_inorder(self.left) +[self.key]+ TreeNode.traverse_inorder(self.right))

    def traverse_preorder(self):
        # root-leftsub-rightsub, break at None:
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right)

    def traverse_postorder(self):
        # left_right_root
        if self is None:
            return []
        return TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key]

    def traverse_level_order(self): #O(N)
        if self is None:
            return None
        list = []
        list.append(self)
        result = []
        while len(list) > 0:
            node = list.pop(0)
            result.append(node.key)
            if node.left:
                list.append(node.left)
            if node.right:
                list.append(node.right)
        return result

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),TreeNode.height(self.right))

    def nodes_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.nodes_size(self.left) + TreeNode.nodes_size(self.right)

    def minimum_depth(self):
        if self is None:
            return 0
        return 1 + min(TreeNode.minimum_depth(self.right), TreeNode.minimum_depth(self.left))

    def diameter(self):
        if self is None:
            return 0
        return max(TreeNode.diameter(self.right), TreeNode.diameter(self.left), (1+TreeNode.height(self.right)+TreeNode.height(self.left)))

    # another way is to use Height() class to record the height of each path
    def is_balanced(self):
        # balanced_tree definitions:
            #  Binary tree in which the height of the two subtrees of every node never differ by more than 1.
        # An empty binary tree is always height-balanced.
        # A non-empty binary tree is height-balanced if:
        # Its left subtree is height-balanced.
        # Its right subtree is height-balanced.
        # The difference between heights of left & right subtree is not greater than 1.
        #https://stackoverflow.com/questions/742844/how-to-determine-if-binary-tree-is-balanced

        if self is None:
            return True
        con1 = TreeNode.is_balanced(self.left)
        con2 =TreeNode.is_balanced(self.right)
        con3 = abs(TreeNode.height(self.left)-TreeNode.height(self.right))<=1
        print(f'con1 {con1} -> con2 {con2} -> con3 {con3} when node  is {self.key}')
        return con1 and con2 and con3

    def __str__(self):
        return(f'{self.key}')

    def __repr__(self):
        return self.__str__()

    def is_BST(self):
        # The left subtree of a particular node will always contain nodes whose keys are less than that node's key.
        # The right subtree of a particular node will always contain nodes with keys greater than that node's key.
        # min,max = None, None
        if self is None:
            return True, None, None
        # if self.left is None and self.right is None:
        #     return True, self.key, self.key
        # root.key must bigger than any nodes on the left subtree and smaller than any nodes on the right subtree
        l_True, l_min, l_max = TreeNode.is_BST(self.left)
        print(f'{l_True},{l_min}, {l_max} : left of {self.key}')
        r_True, r_min, r_max = TreeNode.is_BST(self.right)
        print(f'{r_True},{r_min}, {r_max} : right of {self.key}')

        if l_max is None:
            con1 = True
        else:
            con1 = self.key > l_max
        print(f'{con1}: {self.key} is larger than left_max {l_max} ')

        if r_min is None:
            con2 = True
        else:
            con2 =self.key < r_min
        print(f'{con2} : {self.key} is smaller than right_min {r_min}')


        if l_min is None:
            minimum = self.key
        else:
            if r_min is None:
                minimum = min(self.key, l_min)
            else:
                minimum = min(self.key, l_min, r_min)


        print(f'min is {minimum}: {self.key} node tree')
        if r_max is None:
            maximum = self.key
        else:
            if l_max is None:
                maximum = max(self.key, r_max)
            else:
                maximum = max (self.key, r_max, l_max)
        print(f'max is {maximum}: {self.key} node tree')
        return con1 and con2 and l_True and r_True, minimum, maximum

    ##TODO************: There is another way to do complete_bt using slightly different methods from is_balanced()

    def is_complete_bt(self, index, numOfNodes): # TODO: finish this complete binary tree method, video 3:55
        #https://www.programiz.com/dsa/complete-binary-tree
        if self is None:
            return True
        if index >=numOfNodes:
            print(f'index is {index} and the node is {self.key}')
            return False
        return TreeNode.is_complete_bt(self.left, index*2+1, numOfNodes ) and TreeNode.is_complete_bt(self.right, index*2+2, numOfNodes)

    def is_full_bt(self):
        pass
    # https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
    # https://www.geeksforgeeks.org/binary-heap/
    def is_perfect_bt(self):
        pass

    def is_degenerate_bt(self):
        pass

    def delete(self, node):
        pass



# my_tuple =((1,3,(None,6,(None,10,-1))), 2, ((None, 3, 4), 5, (6, 7, 8)))
# my_tuple = ((1,2,((None,4,5),6, None)),7,(8,9,(10,12, None)))
# my_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
my_tuple = (('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal'))

root = TreeNode.convert_tuple_to_bt(my_tuple)
# root.display_keys()

# print(root.is_binary_search_tree())

