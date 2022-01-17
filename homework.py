

lst = [3, 43, 'shadow', 5, '7', 6]
login = input("Hi new user!\nCreate login: ")
password = input("Create password: ")
name = input("Enter your name: ")
print(f"Hello {name}, you are successfully registered!\n\n")

conf = input(f'{name}, confirm your password to edit list\nLogin: {login}\nPassword: ')
if conf == password:
    add_func = input('1- if append\n2- if insert\n')
    if add_func == '1':
        obj = input('Enter object: ')
        lst.append(obj)
    else:
        obj_ind = int(input('Enter index: '))
        obj = input('Enter object: ')
        lst.insert(obj_ind, obj)
    print(f"new list: {lst}")
else:
    print("Password is incorrect!!!")
