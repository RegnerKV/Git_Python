FILENAME = "task_6.txt"

subjects = {}

try:
    with open(FILENAME, encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subjects[data[0]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print("Неверные данные")

print(subjects)
