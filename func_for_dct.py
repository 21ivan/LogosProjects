def func_for_dct(num):
    dct = {}
    for i in range(0, num):
        while True:
            key = input(f'Enter {i + 1} key: ')
            if key in dct:
                print("This key is already in dict")
                continue
            elif key.isnumeric():
                int_key = int(key)
                if int_key in dct:
                    print("This key is already in dict")
                    continue
                else:
                    value = input(f'Enter {i + 1} value: ')
                    dct[int_key] = value
            else:
                value = input(f'Enter {i + 1} value: ')
                dct[key] = value
            break

    return dct


num = int(input('Enter the count of elements: '))
print(func_for_dct(num))
