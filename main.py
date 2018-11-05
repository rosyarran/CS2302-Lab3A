from RedBlackTree import RedBlackTree
from AVLTree import AVLTree, Node


############# RED-BLACK TREE ###############
def RBT_method():
    user_values = input('Enter insert values with spaces between: ')
    print()

    # Create an RedBlackTree object and add the values
    tree = RedBlackTree()
    for value in user_values.split():
        tree.insert(int(value))

    # Display the height after all inserts are complete.
    print("Red-black tree with " + str(len(tree)) + " nodes has height " + str(tree.get_height()))

    # Read user input to get a list of values to remove
    user_values = input('Enter remove values with spaces between: ')
    print()

    for value in user_values.split():
        to_remove = int(value)
        print('Remove node ' + value + ': ', end='')
        if tree.remove(to_remove):
            print('Red-black tree with ' + str(len(tree)) + ' nodes has height ' + str(tree.get_height()))
        else:
            print('*** Key not found. Tree is not changed. ***')

############# AVL TREE ###############

def AVLT_method():
    # Create an empty AVLTree object.
    tree = AVLTree()

    # Insert some random-looking integers into the tree.
    keys = [10, 20, 5, 22, 15, 47, 19, 3, 12, 18]
    for key in keys:
        node = Node(key)
        tree.insert(node)

    # Print the tree after all inserts are complete.
    print("Tree after initial insertions:")
    print(tree)

    # Find and remove the node with the key value 12.
    # This should cause a right rotation on node 10.
    print("Remove node 12:")
    tree.remove_key(12)
    print(tree)

    # Find and remove the node with the key value 20.
    # This should cause its right child to shift up into
    # the 20 node's position without any other reordering
    # required.
    print("Remove node 20:")
    tree.remove_key(20)
    print(tree)

    # Attempt to remove a node with key 30, a value not in the tree.
    print("Remove node 30 (should not be in tree):")
    if not tree.remove_key(30):
        print("*** Key not found. Tree is not changed. ***")
    print(tree)

############## MAIN #################

user_choice = input(' 1 FOR RED-BLACK TREE\n 2 FOR AVL TREE\n')
print()

if user_choice == "1":
    RBT_method()
elif user_choice == "2":
    AVLT_method()
else:
    print('INVALID')
with open('glove.6B.50d.txt', 'r') as textFile:
    lines = textFile.readlines()
