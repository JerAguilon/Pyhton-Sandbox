class Node(object):
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "{{key: {}, value: {}}}".format(self.key, self.value)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, new_node: Node):
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.left = new_node
            new_node.right = self.head
            self.head = new_node

        self.head.left = self.tail
        self.tail.right = self.head

        self.size += 1


    def pop_back(self):
        if self.size == 0:
            raise Exception("Can't pop an empty list")
        output = self.tail
        self.tail = self.tail.left
        self.size -=1
        if self.size == 0:
            self.head = None
        self.head.left = self.tail
        self.tail.right = self.head
        return output

    def pop_front(self):
        if self.size == 0:
            raise Exception("Can't pop an empty list")
        output = self.head
        self.head = self.head.right
        self.size -=1
        if self.size == 0:
            self.tail = None
        self.head.left = self.tail
        self.tail.right = self.head
        return output

    def move_front(self, node: Node):
        if node == self.head:
            return
        elif node == self.tail:
            temp = self.tail
            self.tail = self.tail.left
            self.head = temp
            return
        else:
            node.left.right = node.right
            node.right.left = node.left

            self.head.left = node
            node.right = self.head

            self.head = node
            self.head.left = self.tail
            self.tail.right = self.head

    def __repr__(self):
        if self.size == 0:
            return str([])
        elif self.size == 1:
            return str([self.head])
        else:
            output = []
            curr = self.head
            while True:
                output.append(curr)
                if curr == self.tail:
                    break
                curr = curr.right
            return str(output)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.ll = LinkedList()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        output = self.cache.get(key, None)
        if not output:
            return -1
        else:
            self.ll.move_front(output)
            return output.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key].value = value
            self.ll.move_front(self.cache[key])
            return

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.ll.push_front(new_node)

        if len(self.cache) > self.capacity:
            node_to_remove = self.ll.pop_back()

            del self.cache[node_to_remove.key]
