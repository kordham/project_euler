def divisors(num):
    sum = 1;
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            sum = sum +i;
    return sum;

def is_abundant(num):
    if(divisors(num)>num):
        return True;
    return False;

def do_loop(list,abundants,num,MAX):
    res_list = list;
    for i in range(num+1):
        if(abundants[i]==1):
            if(i+num<MAX):
                res_list[i+num] = 1;
    return res_list;

import timeit

start = timeit.default_timer()
MAX = 28200;
zeroes_list = [0]*MAX;
abundant_zeroes = [0]*MAX;

for i in range(1,MAX):
    if(abundant_zeroes[i]==0):
        if(is_abundant(i)):
            abundant_zeroes[i] = 1;
            zeroes_list = do_loop(zeroes_list,abundant_zeroes,i,MAX);
sum = 0;

for i in range(MAX):
    if zeroes_list[i] ==0:
        sum = sum + i;
print(sum)
stop = timeit.default_timer()

print('Time: ', stop - start)
