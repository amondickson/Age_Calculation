from datetime import datetime
# Get current date
current_date= datetime.now()
#print(current_date)

#Get User's input
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter you birth day: "))

#Age calculation
age = current_date.year - birth_year - ((current_date.month,current_date.day) < (birth_month,birth_day))

#Calculating remaining months and days
if current_date.month < birth_month or current_date.month == birth_month and current_date.day < birth_day:
    months_remaining = 12 - birth_month + current_date.month - 1
    days_remaining = 30 - birth_day + current_date.day #assuming each month has 30 days
else:
    months_remaining = current_date.month - birth_month
    days_remaining = current_date.day - birth_day

#Result displayal
print(f"You are {age} year(s), {months_remaining} month(s) and {days_remaining} day(s) old")    