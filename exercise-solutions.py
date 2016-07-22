def print_numbers(n):
    if n >= 1:
        print n
        print_numbers(n - 1)

print_numbers(5)


def print_numbers(end, start):
    if end >= start:
        print start
        print_numbers(end, start + 1)

print_numbers(10, 1)

# --------------------------------------
def say_hello(names, i = 0):
    if i < len(names):
        print "Hello, %s!" % names[i]
        say_hello(names, i + 1)

say_hello(['Me', 'You', 'Somebody'])

# --------------------------------------
class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four

def ll_lookup(node, target):
    if node.data == target:
        return node.data
    elif node.next == None:
        return node.next
    else:
        return ll_lookup(node.next, target)



ll_lookup(one, 5)
