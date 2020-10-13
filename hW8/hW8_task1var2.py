class TData:
    t_date = input('Введите дату в формате хх-хх-хххх:_')
    date_list = []

    @classmethod
    def rep_date(cls):
        new_date = TData.t_date.split('-')
        for el in new_date:
            try:
                num = int(el)
            except ValueError:
                return 'Вы ошиблись при вводе! Проверьте данные и попробуйте снова'
            else:
                TData.date_list.append(num)
        return TData.date_list

    @staticmethod
    def check_date():
        TData().rep_date()
        try:
            if TData.date_list[2] not in range(1900, 9999) or TData.date_list[1] not in range(1, 12) or TData.date_list[
                    0] not in range(1, 31):
                return 'Вы ошиблись при вводе! Проверьте данные и попробуйте снова'
            elif TData.date_list[1] == 2 and TData.date_list[0] > 29:
                return 'Вы ошиблись при вводе! Проверьте данные и попробуйте снова'
            elif TData.date_list[1] not in (1, 3, 5, 7, 8, 10, 12) and TData.date_list[0] > 30:
                return 'Вы ошиблись при вводе! Проверьте данные и попробуйте снова'
        except IndexError:
            return 'Вы ошиблись при вводе! Проверьте данные и попробуйте снова'
        else:
            return f'Данные введены корректно. Ваша дата: {TData.t_date.replace("-", " ")}'


print(TData.check_date())
date = TData()
print(date.check_date())