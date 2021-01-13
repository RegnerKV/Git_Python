my_list = ['Привет, мир!\n', '1 2 3\n', 'Hello hello Hello\n']
with open('task_2.txt', 'w+') as file_obj:
    file_obj.writelines(my_list)
with open('task_2.txt') as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count('\n')
        letters = len(line)-1
        print(f'В строке {letters} букв')
    print(f'Всего строк: {lines}')