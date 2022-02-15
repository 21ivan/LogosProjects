import sys


#
# def fun_for_value(arg):
#     return tuple(i for i in arg.values())
#
#
# def fun_for_key(*args, **kwargs):
#     return set(i for i in kwargs), fun_for_value(kwargs)
#
#
# obj_key, obj_value = fun_for_key(name='Tom', one=1, two=2)
#
# print(f'{obj_key}\n{obj_value}')

# lst = ['tom', 'john', 'marusia']
# lst_new = list(map(lambda i: i.title(), lst))
# lst = [1, 2, 3, 4, 5, 6, 7]
# lst_new = list(filter(lambda i: i % 2 == 0, lst))
# print(lst_new)
#
#
# lst = [i for i in range(0, 100000)]
# obj = (i for i in range(0, 100000))
#
# count = 0
# for i in obj:
#     count += sys.getsizeof(i)
# count_lst = 0
# for i in lst:
#     count_lst += sys.getsizeof(i)
# print(count)
# print(count_lst)
# print(sys.getsizeof(lst))
# print(sys.getsizeof(obj))
#
#
#
# def func_gen():
#     for i in [1, 2, 3, 4]:
#         yield i
#
# obj = func_gen()
#
# print(next(obj))
# print(next(obj))


# def number(bus_stops):
#     count = 0
#     for i in range(len(bus_stops)):
#         subtraction = bus_stops[i][0] - bus_stops[i][1]
#         count += subtraction
#     return count
#
#
# num = number([[2, 3], [20, 10]])
# print(num)

def my_2_func_for_list(sm_num):
    dct_in_func = {}
    lst_for_func = []
    for i in range(0, sm_num):
        # lst_for_func = []
        lst_for_func.append(input("Enter key and value pair: ").split(" "))
        # for item in range(len(lst_for_func)):
        dct_in_func = {key: value for key, value in lst_for_func}
    return dct_in_func


my_2dict = my_2_func_for_list(int(input("Enter a number: ")))
print(my_2dict)
