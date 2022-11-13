def winner(time_seq):
    times = len(time_seq) // 2
    left_car_times = time_seq[0: times]
    right_car_times = time_seq[-1:times:-1]
    left_car_total_time = 0
    right_car_total_time = 0

    for current_time in left_car_times:
        current_time = int(current_time)
        if current_time == 0 and left_car_total_time != 0:
            left_car_total_time *= 0.80
        else:
            left_car_total_time += current_time

    for current_time in right_car_times:
        current_time = int(current_time)
        if current_time == 0 and right_car_total_time != 0:
            right_car_total_time *= 0.80
        else:
            right_car_total_time += current_time

    if left_car_total_time < right_car_total_time:
        return f"The winner is left with total time: {left_car_total_time:.1f}"
    elif left_car_total_time > right_car_total_time:
        return f"The winner is right with total time: {right_car_total_time:.1f}"
    else:
        return f"The winner is left/right with total time: {right_car_total_time:.1f}"


time_sequence_input = input().split()
print(winner(time_sequence_input))
