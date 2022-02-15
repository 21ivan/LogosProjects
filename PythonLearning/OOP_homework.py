from faker import Faker

fake = Faker('uk')
lst = []

for n in range(0, 20):
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
        with open(file_name, 'w') as file:
            for item in dct:
                file.write(f'{item} = {dct.get(item)}\n')
        return dct

    @staticmethod
    def func_for_text(file_name):

        _dct_data = {}

        with open(file_name, 'r') as file:
            file.readable()
            for line in file:
                key, value = line.split(' = ')
                _dct_data[key] = value[:-1]
        return _dct_data


obj = Dct(lst, 'My_dict.txt')
print(obj.dct_data)
