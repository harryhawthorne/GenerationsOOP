# Program to learn OOP in Python
# TODO: Create a queue to change current_node and make more generations
import random


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
    for x in range(random.randint(0, 2)):
        new_child = spawn_child(parent, x)

        parent.children.append(new_child)

    return parent.children


def spawn_child(parent, x):
    child = Person(parent.name + str(x), 4, parent.generation + 1, parent)
    print("GEN: " + str(child.generation))
    print("PARENT: " + child.parent.name)
    print("------------")
    return child


def main():
    queue = []
    Grandpa = Person("0", 80, 0, object)
    current_node = Grandpa
    queue.append(current_node)

    while len(queue) > 0:
        returned = spawn_children(current_node)
        queue = returned + queue

        # Print the current queue
        # for i in range(len(queue)):
        #     print(queue[i].name)

        current_node = queue[0]
        queue.pop(0)


# Main in Python
if __name__ == "__main__":
    main()
