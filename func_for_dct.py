def func_for_dct(num):
    dct = {}
    for i in range(0, num):
        key = input(f'Enter {i + 1} key: ')
        value = input(f'Enter {i + 1} value: ')
        dct[key] = value
    return dct


num = int(input('Enter the count of elements: '))
print(func_for_dct(num))
