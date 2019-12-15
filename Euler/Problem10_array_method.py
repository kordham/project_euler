def is_prime(num,list):
    for i in list:
        if(num%i==0):
            return False;
    for j in range(list[len(list)-1],num):
        if(num%j==0):
            return False;

    return True;

number = 2000000;
primes = [2,3]
num = 4;
while(num<number):
    if(is_prime(num,primes)):
        primes.append(num);
    num= num+1
    print(num)
print(sum(primes))
