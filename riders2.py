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
    'sunday': (6, 0.2, 4)
}


def get_possible_rides(rides, available_hour, max_intensity, max_score):
    possible_rides = []
    for ride in rides:
        if ride[2] > available_hour or ride[3] > max_intensity or ride[4] > max_score:
            pass
        else:
            possible_rides.append(ride)
    if possible_rides:
        possible_rides = sorted(possible_rides, key=lambda tup: (tup[1], tup[2], tup[3], tup[4]), reverse=True)
    return possible_rides


def is_valid_ride(ride, available_hour, max_intensity, max_score):
    if ride[2] > available_hour or ride[3] > max_intensity or ride[4] > max_score:
        return False
    return True


def main():
    rides_by_day = {}
    for day, day_ability in CAPABILITIES.items():
        available_hour = day_ability[0]
        max_intensity = day_ability[1]
        max_score = day_ability[2]
        possible_rides = get_possible_rides(RIDES, available_hour, max_intensity, max_score)
        rides_by_day[day] = []
        for ride in possible_rides:
            if is_valid_ride(ride, available_hour, max_intensity, max_score):
                rides_by_day[day].append(ride[0])
                available_hour -= ride[2]
                max_intensity = round(max_intensity-ride[3], 1)
                max_score -= ride[4]
                RIDES.remove(ride)

    print(rides_by_day)





if __name__ == "__main__":
    main()