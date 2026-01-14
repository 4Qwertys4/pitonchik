def read_data(filename):

    people = []

    with open(filename, 'r') as f:
        lines = f.readlines()


    for line in lines:

        parts = line.split()

        date_str = parts[-1]

        day, month, year = map(int, date_str.split('.'))


        surname = parts[0]
        name = parts[1]
        patronymic = parts[2]
        people.append({
            'surname': surname,
            'name': name,
            'patronymic': patronymic,
            'year': year
        })
    return people

def task_a(people):
    count = 0
    print("Жители, родившиеся раньше 1978 года:")
    for person in people:
        if person['year'] < 1978:
            count += 1
            print(f"  - {person['surname']}")
    print(f"Общее число жителей, родившихся раньше 1978 года: {count}\n")

def task_b(people):

    start_year = int(input("Введите начальный год диапазона: "))
    end_year = int(input("Введите конечный год диапазона: "))


    print(f"\nб) Люди, родившиеся в диапазоне {start_year}–{end_year}:")
    found = False
    for person in people:
        if start_year <= person['year'] <= end_year:
            print(f"  {person['surname']} {person['name']} {person['patronymic']} - {person['year']}")
            found = True
    if not found:
        print("  Таких людей не найдено.")

def main():
    filename = "Perepis.txt"
    people = read_data(filename)

    if not people:
        print("Данные не загружены. Проверьте файл.")
        return

    task_a(people)
    task_b(people)

main()