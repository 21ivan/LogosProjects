# class Main:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     @property
#     def get_name(self):
#         return self.__name
#
#     @get_name.setter
#     def get_name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             raise TypeError
#
#     @get_name.deleter
#     def get_name(self):
#         del self.__name

#
# obj = Main('Marusia', 19)
# print(obj.get_name)

#
# class Descriptor:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if self.__name == 'name':
#             if isinstance(value, str):
#                 return instance.__dict__[self.__name]
#             else:
#                 raise TypeError
#         elif self.__name == 'age':
#             if isinstance(value, int):
#                 return instance.__dict__[self.__name]
#             else:
#                 raise TypeError
#         else:
#             return f'{self.__name}'
#
#
# class Main:
#     name = Descriptor()
#     age = Descriptor()
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#
# obj = Main('Marusia', 22)

a = [1, 2, 3, 3]
print(bool(a))
print(type(zip(a)))