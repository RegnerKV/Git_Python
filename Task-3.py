company = {'Иванов': 16500, 'Петров': 28000, 'Сидоров': 13000, 'Антонов': 31000}
try:
    file_obj = open("task_3.txt", 'w')
    for last_name, salary in company.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
sum = 0
count = 0
persons = []
with open("task_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        sum += int(tokens[1])
        count += 1
result = sum / count
print(f"Сотрудники: {persons}")
print(f"Средняя з.п.: {result}")
