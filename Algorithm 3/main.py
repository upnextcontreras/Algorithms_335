# Terry Pham
# CPSC 335
# Section 08
# Github: Tearbear789
# tearbear@csu.fullerton.edu

from typing import List, Tuple

def convert_to_decimal(time: str) -> float:
    """Convert 'HH:MM' time to decimal
    Input:
        A string in 'HH:MM' format.
    Output:
        A float representing the decimal time
    """
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def decimal_to_time(decimal: float) -> str:
    """Convert decimal back to 'HH:MM' format
    Input:
        A float representing the time in decimal hours.
    Output:
        A string in 'HH:MM' format.
    """
    hours, minutes = divmod(int(decimal * 60), 60)
    return f'{hours:02}:{minutes:02}'


def merge_slots(slots: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Sorting and Merge overlapping times
    Input:
        A list of tuples where each tuple contains the start and end time in decimal hours.
    Output:
        A list of merged time slots.
    """
    slots.sort()
    merged = []
    for slot in slots:
        if merged and slot[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], slot[1]))
        else:
            merged.append(slot)
    return merged


def find_available_slots_for_all(
    schedules: List[List[Tuple[str, str]]],
    periods: List[Tuple[str, str]],
    duration: int
) -> List[Tuple[str, str]]:
    """Find common available time slots
    Inputs:
        - A list of lists of busy time intervals for each person.
        - A list of tuples of working periods (start, end) of each person.
        - The duration of the meeting in mins.
    Output:
        A list of available time slots in 'HH:MM' format.
    """
    all_unavailable = [
        (max(convert_to_decimal(time_period[0]), a[0]),
         min(convert_to_decimal(time_period[1]), a[1]))
        for schedule_fill, time_period in zip(schedules, periods)
        for a in merge_slots(
            [(convert_to_decimal(start), convert_to_decimal(end)) 
             for start, end in schedule_fill])
        if a[0] < convert_to_decimal(time_period[1]) and a[1] > convert_to_decimal(time_period[0])
    ]

    merged_unavailable = merge_slots(all_unavailable)

    common_start = max(convert_to_decimal(p[0]) for p in periods)
    common_end = min(convert_to_decimal(p[1]) for p in periods)

    available = [
        (decimal_to_time(a), decimal_to_time(b))
        for a, b in zip(
            [common_start] + [end for _, end in merged_unavailable],
            [start for start, _ in merged_unavailable] + [common_end])
        if b - a >= duration / 60
    ]
    return available


# Example
person1_schedule = [('07:00', '08:30'), ('12:00', '13:00'), ('16:00', '18:00')]
person1_working = ('09:00', '17:00')

person2_schedule = [('09:00', '10:30'), ('12:20', '13:30'), 
                    ('14:00', '15:00'), ('16:00', '17:00')]
person2_working = ('09:00', '18:30')

meeting_duration = 30
# Meeting duration in mins

# Run
available_slots = find_available_slots_for_all(
    [person1_schedule, person2_schedule],
    [person1_working, person2_working],
    meeting_duration
)

# Print
print(available_slots)