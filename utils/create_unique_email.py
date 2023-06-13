from datetime import datetime

current_datetime = datetime.now()
current_year = str(current_datetime.year)
new_string = current_year[2:]
current_time_string = current_datetime.strftime("%m%d%H%M%S")

print(current_time_string)