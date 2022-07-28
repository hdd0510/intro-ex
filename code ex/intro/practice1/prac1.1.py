month = int(input())
year = int(input())
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
if month in [4, 6, 9 ,11]:
    print(30)
elif month in [1,3,5,7,8,10,12]:
    print(31)
else:
    print(29) if is_leap_year(year) == True else print(28) 
