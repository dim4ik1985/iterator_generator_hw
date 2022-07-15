from itertools import chain


# 1. Итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность
#    состоящую из вложенных элементов.
# 3.* Итератор, обрабатывающий списки с любым уровнем вложенности
class MyIterList:

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        self.item = iter(self.obj)
        return self

    def __next__(self):
        next_item = next(self.item)
        if isinstance(next_item, list):
            self.item = chain(next_item, self.item)
            return next(self.item)
        return next_item
