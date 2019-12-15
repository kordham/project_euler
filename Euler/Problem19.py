continuous_date = [1,1,1900,1]

def add_one_day(input_date):
    month_normal = [31,28,31,30,31,30,31,31,30,31,30,31]
    date = input_date;
    if(date[2]%4 ==0 and date[2]!=1900):
        month_normal[1] = 29;
    date[0] = date[0] + 1;
    date[3] = date[3] + 1;
    if(date[3]==8):
        date[3] = 1;
    if(date[0]>month_normal[date[1]-1]):
        date[0] = 1;
        date[1] = date[1] + 1;
    if(date[1]>12):
        date[1] = 1;
        date[2] = date[2] +1;
    return date;
count = 0
while(not(continuous_date[0]==31 and continuous_date[1]==12 and continuous_date[2]==2000    )):
    if(continuous_date[2]>1900 and continuous_date[3]==7 and continuous_date[0]==1):
            count = count +1
    print(continuous_date)
    continuous_date = add_one_day(continuous_date);

print(count)
