class A:
    def data(self):
        pass


class B:
    def data(self):
        pass

    def method(self):
        pass


class C:
    def data(self):
        pass


class D:
    def method(self):
        pass


# lst_class = [A, B, C, D]

# def func_for_find_class(arg):
#     data_dict = {}
#
#     for obj in lst_class:
#         if arg in obj.__dict__:
#             data_dict[obj] = obj.__dict__[arg]
#
#     return data_dict


print((lambda first_name, second_name, lst_obj:
       {obj: obj.__dict__[first_name] for obj in lst_obj if
        first_name in obj.__dict__} |
       {obj: obj.__dict__[second_name] for obj in lst_obj if
        second_name in obj.__dict__})
      ('method',
       'data',
       [A, B, C, D]))

# dct = func_for_find_class('method')
# print(dct)

# class A:
#     def method(self):
#         pass
#
#
# class B:
#     def method(self):
#         pass
#
#     def data(self):
#         pass
#
#
# class C:
#     def method(self):
#         pass
#
#
# class D:
#     def data(self):
#         pass
#
# #
# dich1 = (lambda first_name, second_name, lst_obj: ({key: key.__dict__[first_name] for key in lst_obj if first_name in
#                                                     key.__dict__}, {key: key.__dict__[second_name] for key in lst_obj if
#                                                                     second_name in key.__dict__}))("method", "data",
#                                                                                                    [A, B, C, D])
#
# print(dich1)
#
# dich2 = (lambda first_name, second_name, lst_obj: ({key: key.__dict__[first_name] for key in lst_obj if first_name in
#                                                  key.__dict__}, {key: key.__dict__[second_name] for key in lst_obj if
#                                                                     second_name in key.__dict__}))
# x, y = dich2("method", "data",[A, B, C, D])
# print(f'{x}\n{y}')
# print(y)
