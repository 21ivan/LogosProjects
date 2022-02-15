# def my_2_func_for_list(sm_num):
#     dct_in_func = {}
#     lst_for_func = []
#     for i in range(0, sm_num):
#         # lst_for_func = []
#         lst_for_func.append(input("Enter key and value pair: ").split(" "))
#         # for item in range(len(lst_for_func)):
#         dct_in_func = {key: value for key, value in lst_for_func}
#     return dct_in_func
#
#
# my_2dict = my_2_func_for_list(int(input("Enter a number: ")))
# print(my_2dict)

# rices = list(map(list, (input('Введите значения цен через пробел '))))
print([int(x) if x.isdigit() else x for x in input().split()])

# print(rices)