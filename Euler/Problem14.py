def infinity_loop(num):
    count = 0;
    while(num!=1):
        if(num%2==0):
            num= int(num/2);
        else:
            num = 3*num+1;
        count = count +1;
    return count;

max = 0
biggest = 0;
for i in range(1,1000000):
    current = infinity_loop(i);
    if(max<current):
        max=current;
        biggest = i;

print(big)
