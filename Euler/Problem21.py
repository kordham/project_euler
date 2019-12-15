def sum_divisors(num):
    sum =0 ;
    for i in range(1,int(num/2)+1):
        if ( num%i==0):
            sum = sum + i;
    return sum;

total = 0
for i in range(10000):
    if(sum_divisors(sum_divisors(i))==i and i!=sum_divisors(i)):
        total = total +i;

print(total)
