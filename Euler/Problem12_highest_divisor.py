
import math;

def lin_search(list,item):
    for i in range(len(list)):
        if(list[i]==item):
            return False;

    return True;

def is_triangle(num):
    product = num*2;
    middle = int(math.sqrt(product));
    if (product == middle*(middle+1)):
        return True;
    else:
        return False;

def is_prime(num,list):
    for i in list:
        if(num%i==0):
            return False;
    for j in range(list[len(list)-1],num):
        if(num%j==0):
            return False;

    return True;


def get_product(list):
    product = 1;
    for i in list:
        product = product *i;
    return product;

def get_primes(how_many):
    primes = [2,3]
    num=4;
    while(len(primes)<how_many):
        if(is_prime(num,primes)):
            primes.append(num);
        num= num+1
    return primes;

def exists_smaller(list,max_num):
    for i in list:
        for j in list:
            if(i*j<=max_num and lin_search(list,i*j)):
                list.append(i*j);
                return list;
    return False;


def build_up():
    primes = get_primes(500);
    list = [1];
    while(len(list)<500):
        print(list);
        if(exists_smaller(list,primes[0])==False):
            list.append(primes.pop(0));
        else:
            list = exists_smaller(list,primes[0]);
    return list;
build_up();
