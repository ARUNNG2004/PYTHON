#date_time
import datetime as dt

current_date=dt.date.today()
print(current_date)
#don't change the order of year,month,date
new =dt.date(2022,10,25)
print(new)
print("Year  ",new.year)
print("Month ",new.month)
print("Day   ",new.day)
print("-------------End of date-----------")
#hour,min,sec,mil sec 
a=dt.time(10,2,45,45)
print(a)
print("Hours : ",a.hour)
print("Minute : ",a.minute)
print("Second : ",a.second)
#to find current time
current_time=dt.datetime.now()
print("Current Date and Time",current_time)
print("-------------End of date-----------")
curent=dt.datetime.now()
new_year=dt.datetime(2023,1,1)
difference=new_year-curent
print(difference)
print("-------------End of date-----------")
#using this day month year time
s=curent.strftime("%a %b %B %d %y ")
print(s)