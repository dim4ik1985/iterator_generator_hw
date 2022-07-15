
# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление
def flat_generator(obj, start=0):
    while start < len(obj):
        for item in obj[start]:
            yield item
        start += 1


# 4.* Написать генератор, обрабатывающий списки с любым уровнем вложенности
def mega_flat_generator(obj, start=0):
    while start < len(obj):
        if isinstance(obj[start], list):
            for item in mega_flat_generator(obj[start]):
                yield item
        else:
            yield obj[start]
        start += 1

