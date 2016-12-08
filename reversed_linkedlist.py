class Node(object):
    def __init__(self, value):
        self.payLoad = value
        self.next = None

    def __repr__(self):
        return "Node ({})".format(self.payLoad)

class LinkList(object):
    def __init__(self):
        self.head = None

    def add(self,data):
        temp =  Node(data)
        temp.next = self.head
        self.head = temp

    def search(self,f):
       # If found the element return the corresponding Node
        head = self.head
        found = False
        while head:
            if head.payLoad == f:
                found = head
                break
            head = head.next
        return found

    def __iter__(self):
        # Remember, self is our UnorderedList.
        # In order to get to the first Node, we must do
        current = self.head
        # and then, until we have reached the end:
        while current is not None:
            yield current
            # in order to get from one Node to the next one:
            current = current.next

    def delete(self,d):
        #d - payLoad to be deleted from the LinkList
        #return True if successful otherwise False

        prev, curr = None, self.head
        found = False
        while curr:
            if curr.payLoad == d:
                found = True
                break
            prev = curr
            curr = curr.next
        if found:
            if prev is None: #first Node
                self.head = curr.next #dereferencing pointer to curr
            else:
                prev.next = curr.next #value of prev would be there
            return found
        return found

    def size(self):
        cnt = 0
        head = self.head
        while head:
            cnt +=1
            head = head.next
        return cnt

    def reverse(self):
        #linklist reversed
        prev, nextNode = None, None
        curr = self.head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        self.head = prev

    def peek(self):
        #returns the top of the LinkList
        return self.head.payLoad

    def __repr__(self):
        return "LinkList ({})".format(self.head.payLoad)

a = LinkList()
a.add(10)
a.add(20)
a.add(30)
#iterate over the list like a for loop
for i in a:
    print i
print a.size()
## 30 -> 20 -> 10
assert a.peek() == 30
a.reverse()
## 10->20->30
assert a.peek() == 10
assert a.search(20) is not None
assert a.search(50) == False
assert a.delete(10) == True
assert a.delete(10) == False
