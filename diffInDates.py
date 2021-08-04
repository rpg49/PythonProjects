import datetime
from datetime import date
d1 = datetime.datetime.today().strftime('%Y/%m/%d')
print (d1)
d2 = '2021/07/22'
print (d2)

date1 = datetime.datetime.strptime(d1, '%Y/%m/%d')
print (date1)
date2 = datetime.datetime.strptime(d2, '%Y/%m/%d')
diff = (date1-date2).days
print(diff)