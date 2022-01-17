rand_lst = [2, 4, 11, 34, 78, 980, 'apple', '45', 'bike', 31, 34, 'r', 'sdf']

login = 'admin'
password = 'admin1122'

action = input("Is there a list of random items that you want to do?\n1 - See this list\n2 - Edit this list (you need "
               "to registered)\n->")
while True:
    if action == '2':
        conf_login = input('Enter the login: ')
        conf_password = input('Enter the password: ')
        while login == conf_login and password == conf_password:
            action_for_metods = input('Select a method:\n1 - append\n2 - insert\n3 - extend\n4 - remove\n5 - pop\n'
                                      '6 - index\n7 - count\n8 - sort\n9 - copy\n10 - reverse\n11 - clear\n->')
            if action_for_metods == '1':
                while True:
                    obj = input('Enter element: ')
                    if obj.isnumeric():
                        rand_lst.append(int(obj))
                    else:
                        rand_lst.append(obj)
                    print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break
                    else:
                        print('Wrong choice!!!')
                        break

            elif action_for_metods == '2':
                while True:
                    obj_ind = int(input('Enter index: '))
                    obj = input('Enter object: ')
                    if obj.isnumeric():
                        rand_lst.insert(obj_ind, int(obj))
                    else:
                        rand_lst.insert(obj_ind, obj)
                    # rand_lst.insert(obj_ind, obj)
                    print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '3':
                while True:
                    lst = []
                    n = int(input("Enter number of elements: "))
                    for i in range(0, n):
                        elem = input("Enter element:\n")
                        if elem.isnumeric():
                            lst.append(int(elem))
                        else:
                            lst.append(elem)
                    print(lst)
                    rand_lst.extend(lst)
                    print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '4':
                while True:
                    print(f'Current list before removing:\n{rand_lst}')
                    obj = input('Enter the item you want to remove (if there are 2 or more, are removed first): ')
                    try:
                        obj_num = int(obj)
                        print(f'You input number:{obj_num}')
                        if obj_num in rand_lst:
                            rand_lst.remove(obj_num)
                    except:
                        print(f'You input str:{obj}')
                    if obj in rand_lst:
                        rand_lst.remove(obj)
                    # if type(obj) == int and obj in rand_lst:
                    #     rand_lst.remove(obj)
                    # elif type(obj) == str and obj in rand_lst:
                    #     rand_lst.remove(obj)
                    #     # else:
                    #     #     rand_lst.remove(obj)
                    else:
                        print('this item is not in the list')
                    print('New list after removing:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '5':
                while True:
                    print(f'Current list:\n{rand_lst}')
                    obj = int(input('Enter the index of item you want to remove (if the index is not in the list'
                                    ', are removed last item): '))

                    if obj >= len(rand_lst):
                        print('list index out of range!!!')
                    else:
                        print(f'You removed {rand_lst[obj]} ')
                        rand_lst.pop(obj)
                    print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '6':
                while True:
                    print('Current list:\n', rand_lst)
                    obj = input('Enter element: ')
                    if obj.isnumeric():
                        print('Element index -', rand_lst.index(int(obj)))
                    else:
                        print('Element index -', rand_lst.index(obj))
                    # print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '7':
                while True:
                    print('Current list:\n', rand_lst)
                    obj = input('Enter element: ')
                    if obj.isnumeric():
                        print('The number of items in the list -', rand_lst.count(int(obj)))
                    else:
                        print('The number of items in the list -', rand_lst.count(obj))
                    # print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '8':
                while True:
                    print('List before sorting: ', rand_lst)
                    lst_int = [i for i in rand_lst if type(i) == int]
                    lst_str = [i for i in rand_lst if type(i) == str]
                    rand_lst.clear()
                    lst_int.sort()
                    rand_lst.extend(lst_int)
                    rand_lst.extend(lst_str)
                    print('New sorted list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '9':
                while True:
                    print('Current list', rand_lst)
                    copy_choice = input('Enter 1 -  if you want to copy this list, 2 - back to method selection:\n ')
                    if copy_choice == '1':
                        lst_new = rand_lst.copy()
                        print('New list:\n', lst_new)
                    elif copy_choice == '2':
                        break
                    # print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '10':
                while True:
                    print('Current list', rand_lst)
                    print('New reversed list:\n', rand_lst[::-1])
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

            elif action_for_metods == '11':
                while True:
                    print('Current list', rand_lst)
                    clear_choice = input('Enter 1 -  if you want to clear this list, 2 - back to method selection:\n ')
                    if clear_choice == '1':
                        rand_lst.clear()
                        print('Empty list:\n', rand_lst)
                    elif clear_choice == '2':
                        break
                    # print('New list:\n', rand_lst)
                    begin = input('enter 1 - use this method 2 - back to method selection\n->')
                    if begin == '1':
                        continue
                    elif begin == '2':
                        break

        else:
            print('Password or login are incorrect!!!!')
    elif action == '1':
        print(rand_lst)
        break
    else:
        print('Wrong choice!!!')
        break
