tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
stumped_spaces = tree_height - 1
while tree_height != 0:
    for i in range(spaces):
        print('', end="")
    for i in range(hashes):
        print('', end="")
        print()
        spaces -= 1
        hashes += 2
        tree_height -= 1
    for i in range(stumped_spaces):
        print('', end="")
        print("#")
