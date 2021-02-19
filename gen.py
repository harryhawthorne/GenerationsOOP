# Program to learn OOP in Python
import random
from string import ascii_uppercase as letters

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

    for x in range(random.randint(0,3)):
        new_child = spawn_child(parent,x)
        parent.children.append(new_child)
    return parent.children


def spawn_child(parent,x):

    initial = letters[parent.generation + 1]
    child = Person(initial + str(x), 4, parent.generation + 1, parent)
    print("childs generation: " + str(child.generation))
    print("childs parent:"+ child.parent.name)
    return child

def main():
    Grandpa = Person("A", 80, 0, object)
    current_node = Grandpa
    #
    spawn_children(current_node)

    #Print the name of the current nodes first child
    print(current_node.children[0].name)


# Main in Python
if __name__ == "__main__":
    main()
