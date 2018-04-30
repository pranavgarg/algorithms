import random;

class Domino:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "[{}|{}]".format(self.left, self.right)

def get_random():
    return random.randint(1,6), random.randint(1,6)


def generate_dominos(no):
    dominos = []
    for i in xrange(no):
        left, right = get_random()
        dominos.append(Domino(left, right))
    return dominos

max_count = 0
chain = []
def find_max_dominos(all_dominos, match):
    global max_count
    global chain
    l = len(match)
    if l > max_count:
        max_count = l
        chain = match
    for idx, domino in enumerate(all_dominos):
        rem = all_dominos[:idx] + all_dominos[idx+1:]
        if not match: find_max_dominos(rem, [domino])
        elif domino.left == match[-1].right: find_max_dominos(rem, match + [domino])
        elif domino.left == match[0].left: find_max_dominos(rem, [Domino(domino.right, domino.left)]+ match)
        elif domino.right == match[0].left: find_max_dominos(rem, [domino] + match)
        elif domino.right == match[-1].right: find_max_dominos(rem,match+[Domino(domino.right, domino.left)] )


all_dominos =  generate_dominos(10)
find_max_dominos(all_dominos, [])
print chain


