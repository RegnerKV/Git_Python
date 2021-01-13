def summary():
    try:
        with open('task_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка ввода-вывода')
    except ValueError:
        print('Неправильное значение')
summary()