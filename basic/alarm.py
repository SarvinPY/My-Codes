main_time = input().split(':')
schedule_time = input().split(':')
main_h = int(main_time[0])
main_m = int(main_time[1])
main_s = int(main_time[2])
sch_h = int(schedule_time[0])
sch_m = int(schedule_time[1])
sch_s = int(schedule_time[2])
if main_h <= sch_h < 24  :
    # if main_h == sch_h :
    total_sch = sch_h * 3600 + sch_m * 60 + sch_s
    total_main = main_h * 3600 + main_m * 60 + main_s
    total = total_sch - total_main
    hour = total // 3600
    r = total % 3600
    min = r // 60
    sec = r % 60
if 0 <= sch_h <= main_h :
    if sch_h == main_h :
        if sch_m < main_m :
            total_sch = sch_h * 3600 + sch_m * 60 + sch_s
            total_main = main_h * 3600 + main_m * 60 + main_s
            total = (24 * 3600) - total_main + total_sch
            hour = total // 3600
            r = total % 3600
            min = r // 60
            sec = r % 60
        elif sch_m == main_m and sch_s <= main_s :
            total_sch = sch_h * 3600 + sch_m * 60 + sch_s
            total_main = main_h * 3600 + main_m * 60 + main_s
            total = (24 * 3600) - total_main + total_sch
            hour = total // 3600
            r = total % 3600
            min = r // 60
            sec = r % 60
    else:
        total_sch = sch_h * 3600 + sch_m * 60 + sch_s
        total_main = main_h * 3600 + main_m * 60 + main_s
        total = (24 * 3600) - total_main + total_sch
        hour = total // 3600
        r = total % 3600
        min = r // 60
        sec = r % 60
if hour < 10  :
    hour = '0' + str(hour)
if min < 10 :
    min = '0'+ str(min)
if sec < 10 :
    sec = '0' + str(sec)
print(f'{hour}:{min}:{sec}')