# class A:
#     def __init__(self, *args, **kwargs):
#         self.lst = list(args)
#
#     def method(self):
#         return {i: j for i, j in enumerate(self.lst)}
#
#
# class B:
#     def __init__(self, *args, **kwargs):
#         self.dct = kwargs
#
#     def method(self):
#         return [i for i in self.dct.items()]
#
#
# class C:
#     def __init__(self, *args, **kwargs):
#         self.a = args
#         self.b = args
#
#     def method(self):
#         return self.a ** self.b
#
#
# obj_a = A([1, 4, 3, 2, 1])
# obj_b = B({1: 2, 2: 4})
# obj_c = C(2, 3)
#
# lst_obj = [obj_a, obj_b, obj_c]
#
# lst = []
#
# for i in lst_obj:
#     lst.append(i.method())
# print(lst)
#

#
# class A:
#     pass
#
#
# def func(self, name, age):
#     self.name = name
#     self.age = age
#
#
# def get_result(self, arg):
#     print(f'name = {self.name}\nage = {self.age}')
#
#
# main = type('MainClass', (A,), {'__init__': func,
#                                 '__call__': get_result})
#
# obj = main('Tom', 89)
# obj('python')


def func(some_arg):
    print(some_arg)

a, b = func(('d', 'ds', 'sasa'))