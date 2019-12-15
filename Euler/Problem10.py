def is_prime(num):
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return False;

    return True;

number = 2000000;
num = 2;
sum = 0;
while(num<2000000):
    if(is_prime(num)):
        sum = sum + num;
    print(num)
    num= num+1

print(sum)
