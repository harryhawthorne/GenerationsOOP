# Program to learn OOP in Python
# TODO: Create a queue to change current_node and make more generations
# import random


class Person:

    # Constructor
    def __init__(self, name, age, generation, parent):
        self.age = age
        self.name = name
        self.generation = generation
        self.parent = parent
        self.children = []
        print("hello " + self.name + "!")


def spawn_children(parent):
    for x in range(2):
        new_child = spawn_child(parent, x)

        parent.children.append(new_child)

    return parent.children


def spawn_child(parent, x):
    child = Person(parent.name + str(x), 4, parent.generation + 1, parent)
    print("childs generation: " + str(child.generation))
    print("childs parent:" + child.parent.name)
    print("------------")
    return child


def main():
    queue = []
    Grandpa = Person("0", 80, 0, object)
    current_node = Grandpa
    queue.append(current_node)
    for x in range(20):
        returned = spawn_children(current_node)
        queue.extend(returned)
        queue.pop(0)
        current_node = queue[0]

    # Print the name of the current nodes first child
    # print(current_node.children[0].name)


# Main in Python
if __name__ == "__main__":
    main()
