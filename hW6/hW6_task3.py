par_dic = {}
class Worker:

    name = ''
    surname = ''
    position = ''
    income = 0


    def __init__(self):
        self.name = 'name'
        self.surname = 'surname'
        self.position = 'position'
        self.income = sum(par_dic.values())







class Position(Worker):


    def get_full_name(self):
        self.name = input('Введите Имя сотрудника: _')
        self.surname = input('Введите Фамилию сотрудника: _')
        self.get_total_income()
        print(f'Сотрудник: {self.name} {self.surname}. Совокупный доход: {self.income} рублей')

    def get_total_income(self):
        val_1 = int(input('Введите оклад сотрудника: _'))
        val_2 = int(input('Введите премию сотрудника: _'))
        par_dic['wage'] = val_1
        par_dic['bonus'] = val_2
        self.__init__()




man_1 = Position()
man_1.get_full_name()

