class Road:
    length = 1
    width = 1
    thick = 1


    def __init__(self, length, width, thick):
        self.length = length
        self.width = width
        self.thick = thick

    def gross_w(self):
        first_mass = 25
        gross_weight = length * width * thick * first_mass
        print(f'Вам потребуется {gross_weight/1000} тонн асфальта')


length = int(input('Введите длинну дороги в метрах, которую необходимо построить (м): _'))
width = int(input('Введите ширину дороги в метрах, которую необходимо построить (м): _'))
thick = int(input('Толщина слоя покрытия дороги в сантиметрах, которую необходимо построить (см): _'))


way_1 = Road(length, width, thick)
way_1.gross_w()
