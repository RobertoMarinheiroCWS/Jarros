# Problema dos Jarros

max_x = 4
max_y = 3


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.childrens = []
        self.goal = 0

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.x) + " " + repr(self.y) + "\n"
        for children in self.childrens:
            ret += children.__str__(level + 1)
        return ret

    def fill_up(self, key):  # Fill up - Key = 1 -> fill up X, Key = 0 -> fill up y
        self.childrens.append(Node(max_x, self.y)) if key else self.childrens.append(Node(self.x, max_y))

    def drain_out(self, key):  # Drain out - Key = 1 -> drain out X, Key = 0 -> drain out y
        self.childrens.append(Node(0, self.y)) if key else self.childrens.append(Node(self.x, 0))

    def move(self, key):  # Move - Key = 1 -> move from x to y, Key = 0 -> move from y to x
        if key:
            offerer = self.x
            receiver = self.y
            max_receiver = max_y
        else:
            offerer = self.y
            receiver = self.x
            max_receiver = max_x
        if offerer == 0 or receiver == max_receiver:
            return
        # Move
        receiver_can_receive = max_receiver - receiver
        offer_left_over = offerer - receiver_can_receive
        if offer_left_over < 0:
            offer_left_over = 0
        offer_can_give = offerer - offer_left_over
        new_receiver = receiver + offer_can_give
        new_offer = offerer - offer_can_give
        self.childrens.append(Node(new_receiver, new_offer))

    def expansion(self):
        if (self.x == 0 and self.y == 2) or (self.x == 2 and self.y == 0):  # If is goal, set, and return
            self.goal = 1
            return
        elif self.already_visited():  # Check if this node already been visited (fuck off if it was in this subtree
            # or not) @ToDo -> make this shit better
            return
        visited_list.append(self)  # @Todo -> this sucks
        self.make_movements()  # Make all the possible movements
        for children in self.childrens:
            children.expansion()

    def make_movements(self):  # Make all the possible movements
        self.drain_out(1)
        self.drain_out(0)
        self.move(1)
        self.move(0)
        self.fill_up(1)
        self.fill_up(0)

    def already_visited(self):
        for node in visited_list:
            if node.x == self.x and node.y == self.y:
                return True
        return False


if __name__ == "__main__":
    x = 0
    y = 0  # @ToDo -> Input X and Y
    visited_list = []  # Visited list definition
    root = Node(x, y)  # Root Node definition
    root.expansion()  # Initialize the expansion
    print(root)
