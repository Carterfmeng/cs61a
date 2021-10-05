class ReverseList():

    def __init__(self, item):
        self.list = list(range(item))
        print(self.list)

    def __iter__(self):
        return self

    def next(self):

        try:
            return self.list.pop()
        except:
            raise StopIteration