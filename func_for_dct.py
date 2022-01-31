dct = {}


def func_for_dct(num):
    global dct
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
                    if value.isnumeric():
                        int_value = int(value)
                        dct[int_key] = int_value
                    else:
                        dct[int_key] = value

            else:
                value = input(f'Enter {i + 1} value: ')
                dct[key] = value
            break

    return dct


num = int(input('Enter the count of elements: '))
func_for_dct(num)

with open('My_dict.txt', 'a') as f:
    for item in dct:
        f.write(f'{item} = {dct.get(item)}\n')
