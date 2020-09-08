time = int(input('Введите время в секундах: _'))
hours = time // 3600
minute = (time - (int(hours) * 3600)) // 60
sec = ((time % 3600) - (minute * 60)) % 60
if hours < 10:
    hours = str(str(0) + str(hours))
if minute < 10:
    minute = str(str(0) + str(minute))
if sec < 10:
    sec = str(str(0) + str(sec))

print(f'{time} секунд - это {hours} : {minute} : {sec}')
