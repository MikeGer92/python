class Stationery:

    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


tit = Stationery
tit.draw('')
pen = Pen
pen.draw('n')
penc = Pencil
penc.draw(True)
hand = Handle
hand.draw(None)