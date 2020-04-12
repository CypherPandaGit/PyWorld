import time

print(time.gmtime(0))

local_time = time.localtime()

print(local_time)
print('Year: ', local_time[0], local_time.tm_year)
print('Month: ', local_time[1], local_time.tm_mon)
print('Day: ', local_time[2], local_time.tm_mday)
