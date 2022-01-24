def func_for_dct(num: int):
    dct = {}
    for i in range(0, num):
        key = int(input('Enter key: '))
        value = input('Enter value: ')
        dct[key] = value
    return dct


print(func_for_dct(5))
