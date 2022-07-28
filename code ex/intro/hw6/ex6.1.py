#tạo hàm tính ngày tháng năm sau n ngày 
import datetime

def add_days(cur_date,n):
    # cur_date = datetime.date(year =, day =, month =)
    delta = datetime.timedelta(days=n)
    res = cur_date + delta
    return res