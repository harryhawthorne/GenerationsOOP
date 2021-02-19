# Program to learn OOP and queues in Python
import random


class Person:

    # Constructor
    def __init__(self, name, generation, parent):
        self.name = name
        self.generation = generation
        self.parent = parent
        self.children = []
        print("Hello, " + self.name + "!")


def spawn_children(parent):
    for x in range(random.randint(0, 2)):
        new_child = spawn_child(parent, x)
        parent.children.append(new_child)
    return parent.children


def spawn_child(parent, x):
    # Child has parents name + an extra digit
    child = Person(parent.name + str(x), parent.generation + 1, parent)
    print("GEN: " + str(child.generation))
    print("PARENT: " + child.parent.name)
    print("------------")
    return child


def main():
    queue = []
    Grandpa = Person("0", 0, object)
    current_node = Grandpa
    queue.append(current_node)
    numOfPeople = 1

    while len(queue) > 0:
        newNodes = spawn_children(current_node)
        queue = newNodes + queue
        numOfPeople += len(newNodes)

        # Print the current queue
        # for i in range(len(queue)):
        #     print(queue[i].name)

        current_node = queue[0]
        queue.pop(0)

    print("Number of people in family tree: " + str(numOfPeople))


# Main in Python
if __name__ == "__main__":
    main()
