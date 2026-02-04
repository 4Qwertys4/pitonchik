def read_travels(filename):

    travels = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            parts = line.split()

            day, month, start, end, distance, fuel, weight = parts
            travels.append({
                'day': day,
                'month':month,
                'start': start,
                'end': end,
                'distance': int(distance),
                'fuel': int(fuel),
                'weight': int(weight)
                })

    return travels

def analyze_travels(travels):

    day_totals = {}
    for t in travels:
        day = t['day']
        if day not in day_totals:
            day_totals[day] = 0
        day_totals[day] += t['weight']

    max_day = max(day_totals, key=day_totals.get)
    print(f"Больше всего грузов перевезено {max_day}: {day_totals[max_day]} кг")

    lipki_total = sum(t['weight'] for t in travels if t['start'] == 'Липки')
    print(f"\n2. Масса всех грузов, отправленных из Липок: {lipki_total} кг")

    distance = sum(t['distance'] for t in travels if t['day'] == '1')
    print(f"\n3. Суммарное расстояние за 1 октября: {distance} км")

    print("\n4. Пункты отправления:")
    start_points = {}
    for t in travels:
        if t['start'] not in start_points:
            start_points[t['start']] = 0
        start_points[t['start']] += t['weight']

    print(f"   Количество пунктов отправления: {len(start_points)}")
    print("   Названия и масса грузов:")
    for point, weight in sorted(start_points.items()):
        print(f"    {point}: {weight} кг")

    print("\n5. Пункты назначения:")
    end_points = {}
    for t in travels:
        if t['end'] not in end_points:
            end_points[t['end']] = 0
        end_points[t['end']] += t['weight']

    print(f"   Количество пунктов назначения: {len(end_points)}")
    print("   Названия и масса грузов:")
    for point, weight in sorted(end_points.items()):
        print(f"    {point}: {weight} кг")

    # 6. Пункт назначения с наибольшим средним расходом бензина
    print("\n6. Средний расход бензина по пунктам назначения:")
    end_fuel_stats = {}
    for t in travels:
        if t['end'] not in end_fuel_stats:
            end_fuel_stats[t['end']] = {'total_fuel': 0, 'count': 0}
        end_fuel_stats[t['end']]['total_fuel'] += t['fuel']
        end_fuel_stats[t['end']]['count'] += 1

    # Рассчитываем средний расход
    sr_fuel_by_end = {}
    for point, stats in end_fuel_stats.items():
        sr_fuel = stats['total_fuel'] / stats['count']
        sr_fuel_by_end[point] = sr_fuel

    # Находим пункт с максимальным средним расходом
    max_end = max(sr_fuel_by_end, key=sr_fuel_by_end.get)
    print(f"   Пункт назначения с наибольшим средним расходом: {max_end}")
    print(f"   Средний расход: {sr_fuel_by_end[max_end]:.1f} л")



def main():
    filename = "travels.txt"
    travels = read_travels(filename)

    analyze_travels(travels)


main()