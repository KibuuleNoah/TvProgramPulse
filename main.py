from datetime import datetime, time


def add_mins_to_time(time: time, minutes: int):
    h, m = time.hour, time.minute
    t = h * 60 + m + minutes
    h, m = divmod(t, 60)
    h %= 24
    return datetime.strptime(f"{h}:{m}", "%H:%M").time()


def get_status():
    program_start_tm = time(hour=16, minute=24)
    program_dur = 1
    program_end_tm = add_mins_to_time(program_start_tm, program_dur)
    current_time = datetime.now().time()

    if program_start_tm > current_time:
        print("Upcoming")
    elif program_end_tm < current_time:
        print("Ended")
    else:
        print("Ongoing")


# def add_mins_to_time(time: time, n):
#     s = time.strftime("%I:%M%p")
#     h, m = map(int, s[:-2].split(":"))
#     h %= 12
#     if s[-2:] == "pm":
#         h += 12
#     t = h * 60 + m + n
#     h, m = divmod(t, 60)
#     h %= 24
#     # suffix = "a" if h < 12 else "p"
#     h %= 12
#     # if h == 0:
#     # h = 12
#     return datetime.strptime(f"{h}:{m}", "%H:%M").time()
#


# time_obj = datetime.strptime(time_string, "%I:%M%p").time()
# print(add_mins_to_time("1:20pm", 20), tm)
# print(add_mins_to_time("1:20pm", 20) == tm)
# print(add_mins_to_time("1:20pm", 20) > tm)
# print(add_mins_to_time("1:20pm", 20) < tm)
