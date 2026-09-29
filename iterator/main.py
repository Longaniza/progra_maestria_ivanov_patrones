
from iterator import TreeFactory


tree = TreeFactory().create_tree()

for item in ["A", "B", "C", "D", "E"]:
    tree.add_node(item)


forward_iteator = tree.__iter__()
while True:
    try:
        print(forward_iteator.__next__())
    except StopIteration:
        break

""" for item in tree:
    print(item) """
    
print("----------------")
backward_iteator = tree.__reversed__()
while True:
    try:
        print(backward_iteator.__next__())
    except StopIteration:
        break
""" for item in reversed(tree):
    print(item) """