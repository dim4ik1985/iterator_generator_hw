from iterator_list import MyIterList
from generator_list import flat_generator, mega_flat_generator

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list_max = [
        ['a', 'b', 'c'],
        ['d', ['e1', 'e2', 'e3'], 'f'],
        [1, 2, [None, True, False]],
    ]

    # 1
    # Итератор, который принимает список списков, и возвращает их плоское представление (любой уровень вложенности*)
    print('______________1___________________')
    for item in MyIterList(nested_list):
        print(item)
    # Комперхеншн итератора MyIterList
    flat_list = [item for item in MyIterList(nested_list)]
    print(flat_list)

    print('______________3*___________________')
    for item in MyIterList(nested_list_max):
        print(item)


    print('________________2__________________')

    # 2
    for item in flat_generator(nested_list):
        print(item)
    print('__________________4*_________________')
    for item in mega_flat_generator(nested_list_max):
        print(item)


