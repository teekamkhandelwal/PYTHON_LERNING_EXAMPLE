print('program will print number of days in a given month')
flag=1
month=(int(input('enter the month(1-12)')))
if month==2:
    year=int(input('enter year'))
    if (year%4==0)and(not(year%100==0))or(year%400==0):
        num_days=29
    else:
        num_days=28
elif month in (1,3,5,7,9,11):
    num_days=31
elif month in (4,6,8,10,12):
    num_days=30
else:
    print('please enter valid month')
    flag=0
if flag == 1:
    print('there are',num_days,'days in',month,'month')
