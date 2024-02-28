# For a given list of occupied slots in a company's working hours and a duration for a meeting, finds the first available time slot that is not occupied and allows for the meeting to be held for the given duration.
# Occupied slots with starting and ending times are input in the form of tuples.

from datetime import datetime, timedelta
# Company working hours
START = '8:00' 
END = '17:00'


def find_earliest_slot(occupied_main_list, duration_hours):
    all_slots = set()
    occupied_slots = set()

    # Create a set with all the slots in a working day
    start = datetime.strptime(START, '%H:%M')
    end = datetime.strptime(END, '%H:%M')
    current = start

    while current <= end:
        all_slots.add(current)
        current += timedelta(hours=1)

    # Unpack the main list with the schedules to as single list
    occupied_sub_list = [item for sub_list in occupied_main_list for item in sub_list]

    # Create a set with all occupied slots
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

    # Check for the first available slot
    for i in range(len(sorted_free_slots) - 1):
        current_slot = sorted_free_slots[i]
        next_slot = sorted_free_slots[i + 1]

        available_time = next_slot - current_slot

        if available_time >= duration:
            return f'First available slot: {current_slot.strftime("%H:%M")}'

    return "No available slots"


# print(find_earliest_slot([
#     [('09:00', '11:00'), ('13:00', '15:00')],
#     [('10:00', '12:00'), ('14:00', '16:00')],
#     [('11:00', '15:00')]
# ], 1))

print(find_earliest_slot([
    [('08:00', '17:00')],
    [('08:00', '17:00')],
    [('08:00', '17:00')]
], 1))
