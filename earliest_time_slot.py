# For a given list of occupied slots in a company's working hours and a duration for a meeting, finds the first available time slot that is not occupied and allows for the meeting to be held for the given duration.
# Occupied slots with starting and ending times are input in the form of tuples.

START = '08:00'
END = '17:00'


def convert_str_time_to_int(start_str, end_str):
    start = int(start_str.replace(':', '').lstrip('0'))
    end = int(end_str.replace(':', '').lstrip('0'))

    return start, end


def create_time_set(start_time, end_time):
    time_set = set()

    for i in range(start_time, end_time, 100):
        current = i
        time_set.add(current)

        while current % 100 < 59:
            current += 1
            if current == end_time - 1:
                time_set.add(current)
                break

            time_set.add(current)

    return time_set


def free_hours(occupied_main_list, duration_hours):
    available_hours_str = convert_str_time_to_int(START, END)
    available_hours = create_time_set(available_hours_str[0], available_hours_str[1])
    occupied_hours = set()
    main_occupied_hours = [item for sub_list in occupied_main_list for item in sub_list]

    for slot in main_occupied_hours:
        start = slot[0]
        end = slot[1]
        current_occupied_str = convert_str_time_to_int(start, end)
        current_occupied = create_time_set(current_occupied_str[0], current_occupied_str[1])
        occupied_hours.update(current_occupied)

    available_hours = available_hours.difference(occupied_hours)

    duration = int(duration_hours * 100 if len(str(duration_hours)) == 1
                   else int(str(duration_hours)[0]) * 100 + int(str(duration_hours)[2:]) * 60/10)

    sorted_available_hours = sorted(available_hours)

    for hour in sorted_available_hours:
        start = hour
        end_uncorrected = hour + duration
        end = end_uncorrected if end_uncorrected % 100 < 60 else (end_uncorrected + 40) + (end_uncorrected % 100) - 60

        if end > sorted_available_hours[-1]:
            return "No available slots"

        needed_hours = create_time_set(start, end)

        if needed_hours.issubset(available_hours):
            hour = start // 100
            minutes = start % 100
            hour_as_str = f'0{hour}' if hour < 10 else f'{hour}'
            minutes_as_str = f'{minutes}0' if minutes < 10 else f'{minutes}'

            return f'First available slot: {hour_as_str}:{minutes_as_str}'

    return "No available slots"


# print(free_hours([
#     [('09:00', '11:00'), ('13:00', '15:00')],
#     [('10:00', '12:00'), ('14:00', '16:00')],
#     [('11:00', '15:00')]
# ], 1))

# print(free_hours([
#     [('08:00', '17:00')],
#     [('08:00', '17:00')],
#     [('08:00', '17:00')]
# ], 1))

# print(free_hours([
#     [('09:00', '11:00'), ('13:00', '15:00')],
#     [('10:00', '12:00'), ('14:00', '15:30')],
#     [('11:00', '15:00')]
# ], 1.5))

# print(free_hours([
#     [('08:00', '11:24'), ('13:00', '15:00')],
#     [('16:00', '17:00')]
# ], 1.6))

# print(free_hours([
#     [('08:00', '16:30')],
# ], 1))
