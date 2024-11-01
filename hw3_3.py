#Написать скрипт, который будет выводить текущую дату и время.
from datetime import datetime

cur_time = datetime.now()

print("Текущая дата и время:", cur_time.strftime("%Y-%m-%d %H:%M:%S"))