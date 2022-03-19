import datetime

export_date = '3/18/2022'
#export_date_formatted = datetime.date(export_date)
today = datetime.today()
a = datetime.strptime(export_date, '%-m/%d/%Y')
#print(export_date_formatted)
print(today)
print(a)