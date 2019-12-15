def is_prime(num):
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return False;

    return True;

count = 0;
num = 2;
while(count<10001):
    if(is_prime(num)):
        count = count +1;
    num = num +1;
print(count);
print(num)
