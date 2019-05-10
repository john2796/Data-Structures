
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if not self.value:
            return False
        else:
            if target == self.value:
                return True
            elif target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    def get_max(self):
        if not self.right and not self.left:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        if not self.value:
            return None
        else:
            cb(self.value)
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)
