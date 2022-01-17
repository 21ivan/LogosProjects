# lst = []
#
# for i in range(1, 50, 5):
#     lst.append(i)
# print(lst)
#
# lst_new = [i for i in lst if i % 2 == 0]
# print(lst_new)
#
# n = 'Python'
# if type(n) == str:
#     print('Python == str')


lst = [1, 3, 2, 4, 'q', 'w', 'e', 'r']
# lst_int = [i for i in lst if type(i) == int]
lst_int = []
#lst_str = [i for i in lst if type(i) == str]
lst_str = []
print(lst)
for i in lst:
    if type(i) == int:
        lst_int.append(i)
    else:
        lst_str.append(i)
lst.clear()
lst_int.sort()
lst.extend(lst_int)
lst.extend(lst_str)
print(lst_int)
print(lst_str)
print(lst)
