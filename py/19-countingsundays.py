import calendar
sundays = 0

for year in range(1901, 2001):
    for month in range(12):
        sundays += int(bool(calendar.weekday(year, month+1, 1) == 6))

print(sundays)