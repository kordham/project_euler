def num_divisors(num):
    count =0 ;
    print(str(num), end=" -> ")
    for i in range(1,num+1):
        if ( num%i==0):
            count = count +1;
            print(str(i), end= " ")

    print("\n")
    return count;

x = 1;
i=1
while(num_divisors(x)<500):
    i=i+1
    x=x+i;
print(x);
