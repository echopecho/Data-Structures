class Heap:
    def __init__(self, comparator=[]):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        value_index = len(self.storage) - 1
        self._bubble_up(value_index)

    def delete(self):
        deleted = self.storage[0]
        print(self.storage[-1])
        self.storage[0] = self.storage[-1]
        self.storage.pop(-1)
        print(self.storage)
        self._sift_down(0)
        return deleted
        # store what's at the front
        # put the smallest value at the front, then remove it from our storage
        # call sift down
        # return value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # while index is greater than 0
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = (
                    self.storage[parent],
                    self.storage[index],
                )
            else:
                break

            index = (index - 1) // 2
        # get the parent (i - 1) // 2
        # if child is greater that parent
        # swap them
        # if not, then we're still inside the while loop, but we have nothing to do
        # break

    def _sift_down(self, index):
        while index < len(self.storage) - 1:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = left if self.storage[left] > self.storage[right] else right
            if self.storage[index] < self.storage[largest]:
                self.storage[index], self.storage[largest] = (
                    self.storage[largest],
                    self.storage[index],
                )
            else:
                break

            index = largest

        # while index is less that max index
        # look at both children, choose the biggest
        # left child: 2i + 1
        # right child: 2i + 2
        # swap with that child, if the chosen one is larger, update the index to the new location
        # otherwise break out of your loop


test = Heap()
sample = [6, 8, 10, 9, 1, 9, 9, 5]
for num in sample:
    test.insert(num)
print(test.storage)

test.delete()
print(test.storage)
