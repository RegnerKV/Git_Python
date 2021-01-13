my_list = []
while True:
    line = input("Введите строку: ")
    if line == '':
        print(my_list)
        exit()
    else:
        new_line = line + ' '
        my_list.append(new_line)

    with open('task_1.txt', 'w') as file:
        file.writelines(my_list)
