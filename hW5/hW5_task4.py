from translate import Translator
translator = Translator(to_lang='Russian')
new_list = []
task4 = open('text_4.txt', 'r+', encoding='utf-8')
new_lines = list((task4.read().splitlines()))
for line in new_lines:
    new_list.append(line.split('-'))
for i in range(0, len(new_list)):
    s = (f'{new_lines[i]} - {(translator.translate((new_list[i][0])))}')
    print(s)
    print(s, file=task4)
task4.close()
