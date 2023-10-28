class MyClass:
    def __init__(self):
        self.names = [1, 2, 3, 4]

    def __iter__(self):
        return iter(self.names)

    # for x in self.names:
    #     yield x

    def __next__(self):
        names_copy = self.names
        if names_copy:
            return names_copy.pop()
        else:
            raise StopIteration


f = MyClass()
# for i in f:
#     print(i)
print(next(f))
print(next(f))
print(next(f))
print(next(f))





