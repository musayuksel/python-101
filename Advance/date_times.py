import datetime  # OR
# from datetime import date

# Create a datetime object
uk_entry_time = datetime.datetime(2023, 2, 4, 12, 15, 58)
print(f"uk_entry_time:  {uk_entry_time}")

print(f"NOW: {datetime.datetime.now()}")
print(f"Today: {datetime.date.today()}")

# >>>>>>>>>>>>> DATE TIME METHODS <<<<<<<<<<<<<<<<
print(f"UK entry day: {uk_entry_time.strftime('%d/%m/%Y')}")  # format date
# m : month of the year  # B : month name in full # b : month name in short
print(f"UK entry day: {uk_entry_time.strftime('%A %d %B %Y')}")
print(f"UK entry day: {uk_entry_time.strftime('%A %d %b %Y')}")
print(f"UK entry hour: {uk_entry_time.strftime('%H:%M:%S')}")
