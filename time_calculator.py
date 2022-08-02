
def add_time(start, duration, cur_day = ''):
    
    # converting given string to int
    time_without_period = start.split()[0]
    period = start.split()[1]
    
    h1 = int(time_without_period.split(':')[0])
    m1 = int(time_without_period.split(':')[1])
    
    h2 = int(duration.split(':')[0])
    m2 = int(duration.split(':')[1])
    
    # overall hours and minutes
    sum_h = h1 + h2
    sum_m = m1 + m2
    
    if sum_m > 59:
        sum_m %= 60
        sum_h += 1
    
    # transducing AM/PM, counting days
    days = 0
    
    # AM
    if h2%24 == 0 and m2 == 0 and period == 'AM':
        sum_h = h1
        period = 'AM'
        days = h2/24
    elif sum_h%12==0 and period == 'AM':
        sum_h = 12
        period = 'PM'
    elif sum_h > 12 and period == 'AM':
        sum_h %= 12
        period = 'PM'
        
    # PM
    elif h2%24 == 0 and m2 == 0 and period == 'PM':
        sum_h = h1
        period = 'PM'
        days = h2/24
    elif sum_h%12==0 and period == 'PM':
        days = sum_h/24
        sum_h = 12
        period = 'AM'
    elif sum_h > 12 and period == 'PM':
        days = sum_h/24
        sum_h %= 12
        period = 'AM'

    # converting to str and outputting it
    sum_m = str(sum_m)
    sum_h = str(sum_h)

    # finding a day of the week
    week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 
            'Friday': 4, 'Saturday': 5, 'Sunday': 6}
            
    next_day = ''
    next_pos = 0
    
    # in the case if current day is assigned
    if cur_day:
        key_list = list(week.keys())
        value_list = list(week.values())
        
        cur_pos = value_list.index(week.get(cur_day.capitalize()))
        next_pos = (cur_pos + round(days))%7
        next_day = key_list[next_pos]

        period += ', ' # for proper output

        # return f"{sum_h}:{sum_m.zfill(2)} {period}{next_day} ({round(days)} days later)"

    if 0 < days <= 1:
        return f"{sum_h}:{sum_m.zfill(2)} {period} (next day)"
    elif days > 1:
        return f"{sum_h}:{sum_m.zfill(2)} {period}{next_day} ({round(days)} days later)"
    else:
        return f"{sum_h}:{sum_m.zfill(2)} {period}{next_day}"
        


print(add_time("2:59 AM", "24:00", "saturDay"))