class OwnError(Exception):

    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    def check_err(self):
        try:
            c = int(self.n_1)
            u = int(self.n_2)
            if c < 0 or u < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print('Вы ошиблись при вводе:')
        else:
            exit()


class Storage:
    full_sq = 200
    full_place = 1000
    free_place = 350
    worker = 3
    num_def = 0
    off_eq_dic = [
        (1, {'название': 'Copyr', 'trade_mark': 'Xerox', 'price': 10000, 'unit_count': 3}),
        (2, {'название': 'Printer', 'trade_mark': 'HP', 'price': 8000, 'unit_count': 4}),
        (3, {'название': 'Scanner', 'trade_mark': 'Canon', 'price': 3000, 'unit_count': 5})
    ]

    off_eq_reg_dic = {
        1: ['off_eq_dic_mos', {}],
        2: ['off_eq_dic_kaz', {}],
        3: ['off_eq_dic_ekt', {}],
        4: ['off_eq_dic_serv', {}]
    }

    option_list = {
        1: 'Приход',
        2: 'Расход',
        3: 'Перемещение',
        4: 'инвентаризация',
        5: 'изменение цены',
        6: 'Новый товар'
    }
    class_dic = {1: 'Copyr', 2: 'Printer', 3: 'Scanner', 4: 'Other'}
    trade_mark_list = {1: 'Xerox', 2: 'HP', 3: 'Canon', 4: 'Other'}
    region_list = {1: 'Moscow', 2: 'Kazan', 3: 'Ekaterinburg', 4: 'Service'}

    new_el = {}

    def __init__(self):
        self.option_list = {}
        self.func_list = {}
        self.off_eq_dic = {}
        self.class_dic = {}
        self.trade_mark_list = {}
        self.num_def = 0

    @staticmethod
    def start_work():
        num_def = int(input(f'Введите номер операции {Storage.option_list} для работы со складом: _'))
        if num_def in Storage.func_list:
            if num_def == 1:
                Storage.receipt()
            elif num_def == 2:
                Storage.shipment()
            elif num_def == 3:
                Storage.move()
            elif num_def == 4:
                Storage.invent()
            elif num_def == 5:
                Storage.discount()
            elif num_def == 6:
                Storage.new_el_add()

        else:
            exit()

    @classmethod
    def receipt(cls):
        c = input(f'Какой товар нужно добавить на склад {Storage.class_dic}:_')
        u = input('Введите количество добавляемого товара в шт.:_')
        try:
            c = int(c)
            u = int(u)
            if c < 0 or u < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print('Вы ошиблись при вводе:')
        else:
            Storage.off_eq_dic[c-1][1]['unit_count'] = Storage.off_eq_dic[c-1][1]['unit_count'] + u
            print(Storage.off_eq_dic)

    @classmethod
    def shipment(cls):
        c = input(f'Какой товар нужно отгрузить со складa {Storage.class_dic}:_')
        u = input('Введите количество отгружаемого товара в шт.:_')
        try:
            c = int(c)
            u = int(u)
            if c < 0 or u < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print('Вы ошиблись при вводе:')
        else:
            Storage.off_eq_dic[c - 1][1]['unit_count'] = Storage.off_eq_dic[c - 1][1]['unit_count'] - u
            print(Storage.off_eq_dic)

    @classmethod
    def move(cls):
        c = input(f'Какой товар нужно переместить на склад в Регион {Storage.class_dic}:_')
        u = input('Введите количество перемещаемого товара в шт.:_')
        try:
            c = int(c)
            u = int(u)
            if c < 0 or u < 0:
                raise OwnError("Вы ввели отрицательное число!")
        except ValueError:
            print('Вы ошиблись при вводе:')
        else:
            Storage.off_eq_dic[c - 1][1]['unit_count'] = Storage.off_eq_dic[c - 1][1]['unit_count'] - u
            print(Storage.off_eq_dic)

    @classmethod
    def invent(cls):
        c = int(input(f'Какой товар утрачен на складе {Storage.class_dic}:_'))
        u = int(input('Введите количество утраченного товара в шт.:_'))
        Storage.off_eq_dic[c - 1][1]['unit_count'] = Storage.off_eq_dic[c - 1][1]['unit_count'] - u
        print(Storage.off_eq_dic)

    @classmethod
    def discount(cls):
        c = int(input(f'Укажите, на какой товар цена изменилась {Storage.class_dic}:_'))
        p = int(input('Введите новую цену товара в рублях:_'))
        Storage.off_eq_dic[c - 1][1]['price'] = p
        print(Storage.off_eq_dic)

    @classmethod
    def new_el_add(cls):
        c = int(input(f'Какой товар вы хотите добавить {Storage.class_dic}:_'))
        Storage.new_el['название'] = Storage.class_dic[c]
        t = int(input(f'Выберите марку товара, который вы хотите добавить {Storage.trade_mark_list}:_'))
        Storage.new_el['марка'] = Storage.trade_mark_list[t]
        p = int(input('Введите цену единицы товара в рублях:_'))
        Storage.new_el['цена'] = p
        u = int(input('Введите количество добавляемого товара в шт.:_'))
        Storage.new_el['количество'] = u
        Storage.off_eq_dic.append((len(Storage.off_eq_dic) + 1, Storage.new_el))

    func_list = {
        1: receipt,
        2: shipment,
        3: move,
        4: invent,
        5: discount,
        6: new_el
    }


class OffEq:
    eq_name = ''
    trade_mark = ''
    price = 0
    unit_count = 0

    def __init__(self, eq_name, trade_mark, model, unit_count, price):
        self.eq_name = eq_name
        self.trade_mark = trade_mark
        self.model = model
        self.unit_count = unit_count
        self.price = price


class Copyr(OffEq):
    color = bool
    black = bool


class Printer(OffEq):
    ink_t = bool
    laser_t = bool


class Scanner(OffEq):
    hand_t = bool
    flat_t = bool


num_func = Storage

Storage.start_work()
