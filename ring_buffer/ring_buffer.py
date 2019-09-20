class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.length = 0

  def append(self, item):
    #when capacity is met or exceeded by length
    if self.length == self.capacity:
        self.storage[self.current] = item
        #handles case where current exceeds storage index by resetting current back to 0 which is the oldest item in storage
        if self.current + 1 == self.capacity:
            self.current = 0
        else:
            self.current += 1
        self.increment_length()
    else:
        for index, value in enumerate(self.storage):
            if value is None:
                self.storage[index] = item
                self.increment_length()
                return

  def increment_length(self):
      if self.length == self.capacity:
          return
      else:
          self.length += 1

  def get(self):
    #if else statement optimizes print to only run O(n) list comprehension if the last item is None
    #else it just returns O(1) by returning self.storage
    if self.storage[self.capacity - 1] is None:
        print_array = [item for item in self.storage if item]
        return print_array
    else:
        return self.storage
