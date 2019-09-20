class BinarySearchTree:
      def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

      def insert(self, value):
        #handles case where leaf node is found and value is smaller
        if self.left is None and value <= self.value:
            self.left = BinarySearchTree(value)
        #handles case where leaf node is found and right is smaller
        elif self.right is None and value > self.value:
            self.right = BinarySearchTree(value)
        #repeats first two checks for left node
        elif value <= self.value:
            self.left.insert(value)
        #repeats first two checks for right node
        elif value > self.value:
            self.right.insert(value)


      def contains(self, target):
          if self.value == target:
              return True
          if target > self.value and self.right is not None:
              return self.right.contains(target)
          elif target <= self.value and self.left is not None:
              return self.left.contains(target)
          else:
              return False


      def get_max(self):
        #simply goes to far right node and returns value
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

      def for_each(self, cb):
          cb(self.value)

          if self.left:
              self.left.for_each(cb)
          if self.right:
              self.right.for_each(cb)

      # Print all the values in order from low to high
      # Hint:  Use a recursive, depth first traversal
      def in_order_print(self, node):

          if not node.left:
              print(node.value)

          if node.left and node.right:
              node.in_order_print(node.left)
              print(node.value)
              node.in_order_print(node.right)
          elif node.left:
              node.in_order_print(node.left)
              print(node.value)
          elif node.right:
              node.in_order_print(node.right)
              print(node.value)


      # Print the value of every node, starting with the given node,
      # in an iterative depth first traversal
      def dft_print(self, node):
          stack = Stack()
          stack.push(self)

          current_node = self

          while stack.len() > 0:

              current_node = stack.pop()
              print(current_node.value)
              if current_node.left:
                  stack.push(current_node.left)
              if current_node.right:
                  stack.push(current_node.right)

      # Print the value of every node, starting with the given node,
      # in an iterative breadth first traversal
      def bft_print(self, node):
          queue = Queue()
          queue.enqueue(self)

          current_node = None

          while queue.len() > 0:

              current_node = queue.dequeue()

              if current_node.left:
                  queue.enqueue(current_node.left)
              if current_node.right:
                  queue.enqueue(current_node.right)

              print(current_node.value)


      def pre_order_dft(self, node):
          pass

      def post_order_dft(self, node):
          pass

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
