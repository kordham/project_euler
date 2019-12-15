def is_div(number):
    for i in range(1,21):
        if(number%i!=0):
            return True;
    return False;

num = 21;

while(is_div(num*2520)):
    num=num+1
    print(num*2520)

print(num)
