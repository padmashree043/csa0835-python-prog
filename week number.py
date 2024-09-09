import datetime
year=2015
month=6
day=16
sample_date=datetime.date(year,month,day)
week_number=sample_date.isocalendar()[1]
print(week_number)
