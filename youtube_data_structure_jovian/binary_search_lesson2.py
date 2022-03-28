# video 2:35 Binary Search Trees travelsals and Balancing https://www.youtube.com/watch?v=pkYVOmU3MgA&t=15s&ab_channel=freeCodeCamp.org
'''
TASK: create a data structure-> store 100 million records
perform insertion, search, update and list operations "efficiently".
'''
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
from faker import Faker
from tree_node_binary_search import TreeNode, my_tuple


#***INPUT***: are user profiles: username, name and email
# 100 million users
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        # print('User created!')

    def __repr__(self):
        return(f'User(username={self.username}, name={self.name}, email={self.email})')

    def __str__(self): # by default, this function is not necessary
        return self.__repr__()

class BSTNode(TreeNode):
    def __init__(self, key, value=None):
        super().__init__(key)
        self.value= value
        # for upward traverse
        self.parent = None

    def __str__(self):
        return f'{self.key}: {self.value}'

    def __repr__(self):
        return self.__str__()

def insert_node(tree, key, value):
    # compare with root, if key smaller, recursively check left subtree or attach to left if not existed
    ## method 1 -> return to the tree itself
    if tree is None:
        return BSTNode(key, value)
    if tree.key > key:
        tree.left = insert_node(tree.left, key, value)
        tree.left.parent = tree
    if tree.key < key:
        tree.right = insert_node(tree.right, key,value)
        tree.right.parent = tree
    return tree

def find_node(tree,key):
     if tree is None:
            return None
     if tree.key == key:
        return tree
     if tree.key > key:
        return find_node ( tree.left, key )
     if tree.key < key:
        return find_node ( tree.right, key )



def update_node ( tree, key, value ):
    node = find_node ( tree, key )
    if node is not None:
        node.value = value
    return tree

def list_all_nodes(tree): # video 3:55
    if tree is None:
        return []
    return list_all_nodes(tree.left) + [(tree.key, tree.value)] + list_all_nodes(tree.right)


def make_balanced_bst_from_sorted_list(data, lo=0, hi=None, parent=None):
        if data is None:
            return None
        if hi is None:
            hi = len(data)-1
        if lo > hi:
            return None

        mid = (hi+lo)//2
        key, value = data[mid]

        root = BSTNode(key, value)
        root.parent = parent
        root.left = make_balanced_bst_from_sorted_list(data, lo, mid-1, root)
        root.right = make_balanced_bst_from_sorted_list(data, mid+1, hi, root)

        return root

users = [
    ('aaa','for aaa'),
    ('bbb','for bbb'),
    ('ccc','for ccc'),
    ('ddd','for ddd'),
    ('ppp','for ppp'),
    ('ttt','for ttt'),
    ('zzz','for zzz')
]

mybst =make_balanced_bst_from_sorted_list(users)
# BSTNode.display_keys(mybst)
# print(BSTNode.is_balanced(mybst))


nancy = User("nancybest","nancy", "nancy@gmail.com")
soba =User('mom', 'sobatith', 'sobathie@yahoo.com')
abash = User('abashsmith', 'Abash', 'abash@mail.com')

zoney =User('zoney', 'zone','zone@gmail.com')
aaa = User('aka', 'aaabrain', 'aaa@mail.com')
zzz = User('zzz', "zzz", 'zzz@mail.com')
bush = User('bush', 'bushSimth', 'bush_smith@mail.com')
josh = User('mut', 'mugHamilton', 'mug_hamilton@gmail.com')
xray = User('xray','xraySpecialist', 'xray_specialish@yahoo.com')
users = []
tree =(('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal'))
node = BSTNode('nancybest', nancy)


insert_node(node, soba.username, soba)
insert_node(node, abash.username, abash)
insert_node(node, zoney.username, zoney)
insert_node(node, aaa.username, aaa)
insert_node(node, zzz.username,zzz)
insert_node(node, bush.username,bush)
# node.insert_node(node, josh.username, josh)
insert_node(node, xray.username,xray)



# node.display_keys()
# is_bst_node=is_bst, min, max =node.is_binary_search_tree()
# print(node.height())
# print(find_node(node, abash.username))
update_node(node, abash.username, User('abashsmith', 'AbashSamul', 'abash_samul@mail.com'))
# node.display_keys()
# print(node.find_node(abash.username))
numOfNodes = node.nodes_size()
# print(node.is_complete_bt(0, numOfNodes))
list = list_all_nodes(node)
# print(len(list))
root =make_balanced_bst_from_sorted_list(list, 0)
# root.display_keys()
# print(root.is_balanced())
# root = BSTNode.convert_tuple_to_bt(my_tuple)
# root.display_keys()
# print(root.is_binary_search_tree())




#***OUTPUT***: is the data structure that store all user profiles,
# and have four methods ==> insert a user, find a user, update a user and list_all users
class UserDatabase:
    def __init__(self):
        # purpose: to store the User objects in a list sorted by usernames
        self.users = []
    # four methods
    def insert(self, user):
        # Loop through the list and add the new user at a position that keeps the list sorted by username
        # *** O(N) *** --> brute force method
        # i = 0
        # while i < len(self.users):
        #     if user.username < self.users[i].username:
        #         break
        #     i += 1
        # self.users.insert(i,user)
        # O(lgN)
        start = 0
        end = len(self.users)-1
        mid = 0
        while start<= end:
            mid = (start + end)//2
            # print(f'mid is {mid}, the user is {self.users[mid].username}')
            if self.users[mid].username.casefold() == user.username.casefold():
                # print("username existed, can't insert this user into the database")
                return
            elif self.users[mid].username.casefold() > user.username.casefold():
                # print("in the left half ")
                end = mid-1
            elif self.users[mid].username.casefold() < user.username.casefold():
                # print('in the right half')
                start = mid + 1
                if start >= len(self.users):
                    mid=len(self.users)


        self.users.insert(mid, user)
        # print(f'{user} has been inserted into position {mid}')

    def find(self, user):

        # BAD COMPLEXITY - O(N) - brute force method
        # lo, hi = 0, len(self.users)-1
        # if hi == 0:
        #     print('the db is empty')
        #     return None
        # usernames = []
        # for u in self.users:
        #     usernames.append(u.username)
        # index = binary_search(lo,hi,user.username, usernames)
        # return self.users[index]

        start = 0
        end = len(self.users) - 1
        while start <= end:
            mid = (start + end) // 2
            # print(f'mid is {mid}, the user is {self.users[mid].username}')
            if self.users[mid].username.casefold() == user.username.casefold():
                print(f"found {user} at {mid}")
                return self.users[mid]
            elif self.users[mid].username.casefold() > user.username.casefold():
                # print("in the left half ")
                end = mid - 1
            elif self.users[mid].username.casefold() < user.username.casefold():
                # print('in the right half')
                start = mid + 1
        print("can't find this user")
        return None


    def update(self, user): # the username with updated email and name properties
        #senarios:
        # username is not existed
        # username is existed
        # database is empty
        # email valide format or not -> follow the update or stop
        #

        target = self.find(user)
        if target:
            target.name, target.email = user.name, user.email
        else:
            print("no such user in update()")

    def list_all(self):
        #senarios:
        # data base is empty
        #
        return self.users


#
# fake = Faker()
# db = UserDatabase()
# for i in range(10000):
#     username= fake.name()
#     db.insert(User(username, username, username+'email.com'))

# CPU times: total: 30.7 s
# Wall time: 28.7 s

# print('nancybest'>'sobathie')

# Come up with some sample inputs and outputs for testing
# aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
# biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
# hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
# jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
# siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
# sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
# vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
#
# users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]




# db = UserDatabase()
# for _ in range(1000000):
#     user = User(username=Faker.name(), name=Faker.name(), email=Faker.email())
#     db.insert(user)
#
# db.update(User(username='sonaksh', name='SONY', email='SONY@mail.com'))
# db.find('nancy')
# db.insert(User(username='nancy', name='nancy', email='nancy@mail.com'))
# db.find('luch')
# print(db.list_all())




def binary_search(lo, hi, username, list):
    while lo <= hi:
        mid = (lo + hi) //2
        # 3 possible outcomes
        if list[mid] == username:
            return mid
        elif list[mid] > username:
            hi = mid -1
        else:
            lo = mid +1
    print("no such username in find()")
    return -1

# user = db.find("hemanth")
# test = {
#     'input': {
#         'username': "hemanth"
#     },
#     'output': 'hemanth@example.com'
# }
# evaluate_test_case(db.find, test)
# print(user)
