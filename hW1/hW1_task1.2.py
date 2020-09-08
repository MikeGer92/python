time = int(input('Введите время в секундах: _'))
hours = time // 3600
if hours < 10:
    hours = str(str(0) + str(hours))
minute = (time - (int(hours) * 3600)) // 60
sec = ((time % 3600) - (minute * 60)) % 60

print(f'{time} секунд - это {hours} : {minute} : {sec}')
