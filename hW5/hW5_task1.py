
file_name = input('Введите название файла: _')
f = open(f'{file_name}.txt', 'a', encoding='utf-8')
while True:
    s = input('Вводимые данные: ')
    if s == '':
        break
    f.writelines(s+'\n')
print(f'Ваши данные записаны в файл {file_name} и сохранены')
f.close()
