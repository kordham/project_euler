def num_divisors(num):
    count =0 ;
    for i in range(1,num+1):
        if ( num%i==0):
            count = count +1;

    return count;
import timeit

start = timeit.default_timer()

MIN = 500;
for i in range(100000):
    if(i%2==0):
        if((num_divisors(int(i/2)))*num_divisors(i+1)>MIN):
            print(i);
            print(str(i*(i+1)/2))
            #print(num_divisors(int(i*(i+1)/2)))
            break;
    else:
        if((num_divisors(int(i)))*num_divisors(int((i+1)/2))>MIN):
            print(str(i*(i+1)/2))
            #print(num_divisors(int(i*(i+1)/2)))
            break;

stop = timeit.default_timer()

print('Time: ', stop - start)
