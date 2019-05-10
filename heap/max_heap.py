class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

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

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self._swap(index, parent)
            index = parent

    def _sift_down(self, index):
        while index < len(self.storage) - 1:
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child <= len(self.storage) - 1 and right_child <= len(self.storage) - 1:
                if self.storage[left_child] > self.storage[right_child]:
                    if self.storage[index] < self.storage[left_child]:
                        self._swap(index, left_child)
                else:
                    if self.storage[index] < self.storage[right_child]:
                        self._swap(index, right_child)
            elif left_child <= len(self.storage) - 1:
                if self.storage[index] < self.storage[left_child]:
                    self._swap(index, left_child)
            index += 1

    def _swap(self, x, y):
        self.storage[x], self.storage[y] = self.storage[y], self.storage[x]
