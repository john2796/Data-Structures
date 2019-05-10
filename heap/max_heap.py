class Heap:
    def __init__(self):
        self.storage = []

# Add value to end of array
# Float it Up to its proper position
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)  # pass index of last item

    def _bubble_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                # swap pos if true then repeat until false
                self._swap(index, parent)
            index = parent  # then asign index to be the new parent

    def delete(self):
        if not len(self.storage):
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            current_max = self.storage[0]
            self.storage[0] = self.storage.pop()
            self._sift_down(0)
            return current_max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _sift_down(self, index):
        while index < len(self.storage) - 1:
            left = 2 * index + 1
            right = 2 * index + 2

            if right <= len(self.storage) - 1 and self.storage[left] < self.storage[right]:
                self._swap(index, right)
            elif left <= len(self.storage) - 1 and self.storage[index] < self.storage[left]:
                self._swap(index, left)
            index += 1

    def _swap(self, x, y):
        self.storage[x], self.storage[y] = self.storage[y], self.storage[x]
