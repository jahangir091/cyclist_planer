RIDES = [
        (1, 1, 7, 0.2, 40),
        (2, 2, 4, 0.1, 15),
        (3, 3, 1, 0.2, 25),
        (4, 4, 3, 0.1, 10),
        (5, 5, 2, 0.3, 18)
    ]

CAPABILITIES = {
    'monday': (3, 0.4, 40),
    'tuesday': (1, 0.1, 50),
    'wednesday': (4, 0.3, 30),
    'thursday': (1, 0.5, 60),
    'friday': (2, 0.2, 25),
    'saturday': (4, 0.6, 20),
    'sunday': (6, 0.2, 40)
}


def get_possible_days(capabilities, ride):
    possible_days = {day: ability for day, ability in capabilities.items() if ability[1] >= ride[3] and ability[2] >= ride[4]}
    sorted_possile_days = {day: ability for day, ability in sorted(possible_days.items(), key=lambda item: (abs(item[1][0]-ride[2]), item[1][1]-ride[3], item[1][2]-ride[4]), reverse=False)}
    return sorted_possile_days


def main():
    rides_by_day = {}
    for ride in RIDES:
        possible_days = get_possible_days(CAPABILITIES, ride)
        if possible_days:
            day = list(possible_days)[0]
            del CAPABILITIES[day]
            rides_by_day[day] = ride[0]

    print(rides_by_day)


if __name__ == "__main__":
    main()