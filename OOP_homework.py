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

from faker import Faker

fake = Faker('uk')
lst = []

for n in range(0, 25):
    lst.append(fake.name())


class Dct:

    def __init__(self, args, file_name):
        self.dct = self.add_to_file(args, file_name)
        self.dct_data = self.func_for_text(file_name)

    @staticmethod
    def add_to_file(args, file_name):
        dct = {}
        for i, j in enumerate(args):
            dct[i+1] = j
        with open(file_name, 'a') as file:
            for item in dct:
                file.write(f'{item} = {dct.get(item)}\n')
        return dct

    @staticmethod
    def func_for_text(file_name):

        _dct_data = {}

        with open(file_name, 'r') as file:
            for line in file:
                if line == '=':
                    continue
                key, *value = line.split(' = ')
                _dct_data[key] = value
        return _dct_data


obj = Dct(lst, 'My_dict.txt')
print(obj.dct_data)
