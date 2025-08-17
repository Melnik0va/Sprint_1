time_string=('1h 45m,360s,25m,30m 120s,2h 60s')
time_values=time_string.split(',')
time_summ=0

for value in time_values:
    value=value.split()
    for time in value: 
        if 'h' in time:
            time_summ+=int(time.replace('h',''))*60
        if 'm' in time: 
            time_summ+=int(time.replace('m',''))
        if 's' in time: 
            time_summ+=int(time.replace('s',''))/60

print('Общее время в минутах:', int(time_summ))