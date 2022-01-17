num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))

sign = input('enter sign: ')
if sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/':
    if num2 == 0:
        print('Error!!! ZeroDivision')
    else:
        print(num1 / num2)
######################################################
######################################################
lst = [1, 2, 3, 4, 5]
lst_new = lst.copy()
lst.clear()
print(lst)
print(lst_new)
lst = [1, 3, 4, 5, 6]

add_func = input('1 - if append\n 2- if insert ')
if add_func == '1':
    obj = input('Enter object')
    lst.append(obj)
else:
    obj_ind = int(input('Enter index:'))
    obj = input('Enter object')
    lst.insert(obj_ind, obj)
print(lst)

# lst = [1, 3, 4, 5, 6]
# login = input("Hi new user!\nCreate login: ")
# password = input("Create password: ")
# name = input("Enter your name: ")
# print(f"Hello {name}, you are successfully registered!\n\n")
#
# conf = input(f'{name}, confirm your password to edit list\nLogin: {login}\nPassword: ')
# if conf == password:
#     add_func = input('1- if append\n2- if insert\n')
#     if add_func == '1':
#         obj = input('Enter object: ')
#         lst.append(obj)
#     else:
#         obj_ind = int(input('Enter index: '))
#         obj = input('Enter object: ')
#         lst.insert(obj_ind, obj)
#     print(f"new list: {lst}")
# else:
#     print("Password is incorrect!!!")
