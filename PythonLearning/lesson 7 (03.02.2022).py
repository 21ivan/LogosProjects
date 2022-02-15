class Safe:
    def write_balance(self, balance):
        with open('balance.txt', 'w') as file:
            file.write(f'{balance}')

    def get_balance(self):
        with open("balance.txt", 'r') as file:
            return file.read()


class Bankomat(Safe):
    pin = 1111

    def __init__(self, money):
        self.write_balance(money)
        self.pin_valid()

    def pin_valid(self):
        count = 0
        while count <= 3:
            if count == 3:
                print('The end')
                break
            try:
                user_pin = int(input('Enter password: '))
            except ValueError:
                count += 1
                continue
            else:
                if user_pin == self.pin:
                    self.info_for_user()
                else:
                    count += 1
                    continue

    def info_for_user(self):
        user_choice = int(input('1: Get money\n2: Get balance\n3: Exchange rate\n4: Exit\n'))
        if user_choice == 1:
            self.balance()
        elif user_choice == 2:
            self.give_me_money()
        elif user_choice == 3:
            self.rate()
        elif user_choice == 4:
            self.exit()

    def balance(self):
        print(self.get_balance())

    def give_me_money(self):
        sum_money = int(input('Enter money you take: '))
        if sum_money <= int(self.get_balance()):
            self.write_balance(int(self.get_balance()) - sum_money)
            print(self.balance())
        else:
            print('You don`t have some money')

    def exit(self):
        choice_for_exit = int(input('If you want exit press 0:\n'))
        if choice_for_exit != 0:
            return self.exit()
        else:
            return 'Bye'


user = Bankomat(10000)
