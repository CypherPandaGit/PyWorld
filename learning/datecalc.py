# import time
#
# print(time.gmtime(0))
#
# local_time = time.localtime()
#
# print(local_time)
# print('Year: ', local_time[0], local_time.tm_year)
# print('Month: ', local_time[1], local_time.tm_mon)
# print('Day: ', local_time[2], local_time.tm_mday)

#-----------------------------------------------------

import time
from time import time as my_timer
import random

input('Press enter to start')

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press enter to stop')

end_time = my_timer()

print('Started at ' + time.strftime('%X', time.localtime(start_time)))
print('Ended at ' + time.strftime('%X', time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds.")
