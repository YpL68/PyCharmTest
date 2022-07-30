from datetime import datetime, timedelta

users = [
    {"name": "Воскресенье", "birthday": datetime(2062, 7, 31)},
    {"name": "Суббота", "birthday": datetime(2072, 7, 30)},
    {"name": "Шевченко", "birthday": datetime(2062, 7, 29)},
    {"name": "Ребров", "birthday": datetime(2072, 8, 1)},
    {"name": "Блохин", "birthday": datetime(2072, 8, 1)},
    {"name": "Марадонна", "birthday": datetime(2092, 8, 2)},
    {"name": "Пеле", "birthday": datetime(2062, 8, 3)},
    {"name": "Гусин", "birthday": datetime(2072, 8, 4)},
    {"name": "Базилевич", "birthday": datetime(2072, 8, 5)},
    {"name": "Воскресенье1", "birthday": datetime(2062, 8, 6)},
    {"name": "Суббота1", "birthday": datetime(2072, 8, 7)},
    {"name": "Михайличенко", "birthday": datetime(2092, 8, 8)}]


def get_birthdays_per_week(users_list: list):
    num_days = 7
    date_start = datetime.now()

    if date_start.weekday() == 0:
        date_start += timedelta(days=-2)

    work_days_with_lists = {(date_start + timedelta(days=nd)).weekday():
                                {"name_day": (date_start + timedelta(days=nd)).strftime("%A"), "people_list": []}
                            for nd in range(num_days) if (date_start + timedelta(days=nd)).weekday() < 5}

    birth_days_links = \
        {((date_start + timedelta(days=nd)).month, (date_start + timedelta(days=nd)).day):
             (date_start + timedelta(days=nd)).weekday() if (date_start + timedelta(days=nd)).weekday() < 5 else 0
         for nd in range(num_days)}

    for pos in users_list:
        week_day = birth_days_links.get((pos["birthday"].month, pos["birthday"].day))
        if week_day is not None:
            work_days_with_lists[week_day]["people_list"].append(pos["name"])

    for val in work_days_with_lists.values():
        if len(val["people_list"]):
            name_day = val["name_day"]
            list_people = ", ".join(sorted(val["people_list"]))
            print(f"{name_day}: {list_people}")


if __name__ == '__main__':
    get_birthdays_per_week(users)
