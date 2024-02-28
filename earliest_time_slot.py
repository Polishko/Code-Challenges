from datetime import datetime, timedelta
START = '8:00'
END = '17:00'


def find_earliest_slot(occupied_main_list, duration_hours):
    all_slots = set()
    occupied_slots = set()

    start = datetime.strptime(START, '%H:%M')
    end = datetime.strptime(END, '%H:%M')
    current = start

    while current <= end:
        all_slots.add(current)
        current += timedelta(hours=1)

    occupied_sub_list = [item for sub_list in occupied_main_list for item in sub_list]

    for slot in occupied_sub_list:
        start = datetime.strptime(slot[0], '%H:%M')
        end = datetime.strptime(slot[1], '%H:%M')

        current = start

        while current <= end:
            occupied_slots.add(current)
            current += timedelta(hours=1)

    free_slots = all_slots.difference(occupied_slots)
    sorted_free_slots = sorted(free_slots)

    duration = timedelta(hours=duration_hours)

    for i in range(len(sorted_free_slots) - 1):
        current_slot = sorted_free_slots[i]
        next_slot = sorted_free_slots[i + 1]

        available_time = next_slot - current_slot

        if available_time >= duration:
            return f'First available slot: {current_slot.strftime("%H:%M")}'

        return "No available slots"


print(find_earliest_slot([
    [('09:00', '11:00'), ('13:00', '15:00')],
    [('10:00', '12:00'), ('14:00', '16:00')],
    [('11:00', '15:00')]
], 1))
