# def recursive_func(n):
#     if n == 1:
#         return n
#     else:
#         return n * recursive_func(n - 1)
#
#
# print(recursive_func())

# recursive = lambda n: n if n == 1 else n * recursive(n - 1)
#
# print(recursive(5))

# func = lambda n: 1 if n < 2 else func(n - 1) + func(n - 2)
#
#
# def func(n):
#     if n < 2:
#         return 1
#     else:
#         return func(n - 1) + func(n - 2)
#
#
# print(func(10))
# import sys
#
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())


# def main_func(n):
#     def first_func():
#         print('first func')
#     def second_func():
#         print('second func')
#     return first_func() if n==1 else second_func()
#
# obj = main_func(1)


####Decorator####
# import functools
#
#
# def deco():
#     def main_func(func):
#         print('after main_func')
#         @functools.wraps(func)
#         def wrapper():
#             print('in wrapper')
#             return func()
#             print('after func')
#         return wrapper
#
# @deco()
# def another_func(name):
#     print(f'my name is {name}')
#
# another_func('dsfsdgs')
# #
#
#
with open("my_file.txt", 'w') as f:
    f.write()