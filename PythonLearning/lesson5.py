# def func_for_text(name_text):
#     dct_data = {}
#
#     with open(name_text, 'r') as f:
#
#         text = ''.join(i.lower() for i in f.read() if i.isalpha())
#     for i in text:
#         if i not in dct_data:
#             dct_data[i] = 1
#         else:
#             dct_data[i] +=1
#     return dct_data
#
# print(func_for_text("my_file.txt"))

# def func(*args, **kwargs):
#     dct = {}
#     assert len(args) > 0, 'len(args) == 0'
#     for i, j in enumerate(args, 1):
#         dct[i] = j
#     return dct
#
#
# print(func(1, 2, 3, 4))

#
# class Dog:
#     n = 'python'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# jack = Dog('Jack', 3)
# lokky = Dog('Lokky', 2)
#
# print(jack)
#
from faker import Faker

fake = Faker('uk')
lst = []

for i in range(0, 20):
    lst.append(fake.name())


class Dct:

    def __init__(self, args):
        self.dct = self.for_dct(args)
    def for_dct(self, args):
        dct = {}
        for i, j in enumerate(args):
            dct[i+1] = j
        return dct

    def func_for_text(self, args):
        dct_data = {}

        with open(args, 'r') as f:

            text = ''.join(i.lower() for i in f.read() if i.isalpha())
        for i in text:
            if i not in dct_data:
                dct_data[i] = 1
            else:
                dct_data[i] += 1
        return dct_data


obj = Dct(lst)

print(obj.func_for_text('my_file.txt'))

print(obj.dct)


#########
# class Color:
#     red = 0
#     green = 0
#     blue = 0
#
#     def __init__(self, red, green, blue):
#         self.red = red
#         self.green = green
#         self.blue = blue
#
#     def toHex(self):
#         return '#%02x%02x%02x' % (red, green, blue)
#
#
# class ColorAlpha(Color):
#     alpha = 1
#
#     def __init__(self, red, green, blue, alpha):
#         self.red = red
#         self.green = green
#         self.blue = blue
#         self.alpha = alpha
#
# gray = Color(80, 80, 80)

# class Smartphone:
#     def __init__(self, model = 'Unknown', storage_size = 'Unknown', battery = 'Unknown'):
#         self.model = model
#         self.storage_size = storage_size
#         self.battery = battery
#
#     def info(self):
#         print(f'{self.model}\n{self.storage_size}\n{self.battery} ')
#
#
#
# iphone = Smartphone('Iphone', 64, 3200)
# samsung = Smartphone('Samsung', 128, 6400)
# iphone.info()
# samsung.info()